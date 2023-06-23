# Standard libs
from typing import Dict

# Django imports
from django.conf import settings
from django.utils.timezone import now

# DALEC imports
from dalec.proxy import Proxy
from nextcloud import NextCloud

client = NextCloud(
    endpoint=settings.DALEC_NEXTCLOUD_BASE_URL,
    user=settings.DALEC_NEXTCLOUD_API_USERNAME,
    password=settings.DALEC_NEXTCLOUD_API_PASSWORD,
)


class NextcloudProxy(Proxy):
    """
    nextcloud dalec proxy to fetch the last messages.
    """

    app = "nextcloud"

    def _fetch(
        self, nb: int, content_type: str, channel: str, channel_object: str
    ) -> Dict[str, dict]:
        if content_type == "activity":
            return self._fetch_activity_file(nb, channel, channel_object)

        raise ValueError(f"Invalid content_type {content_type}. Accepted: activity.")

    def _fetch_activity_file(self, nb, channel=None, channel_object=None):
        """
        Get latest activities from entire nextcloud or channel
        """
        options = {"limit": nb}

        if channel:
            if channel not in ["files", "files_and_childs"]:
                raise ValueError(
                    """Value `{}` is not a correct value for channel type and Activity.
                    It must be either : files, files_and_childs or None.
                    """.format(
                        channel
                    )
                )
            if not channel_object:
                raise ValueError("""channel_object must be provided together with channel""")
        elif channel_object:
            raise ValueError("channel must be provided together with channel_object")

        if channel == "files":
            # retrieve only activity of one file/folder
            file_id = client.get_file(channel_object)
            activities = client.get_activities(
                **options, object_type="files", object_id=file_id
            ).data
        elif channel == "files_and_childs":
            # retrieve activity of a folder and sub-directories/files recursively
            # get base path

            try:
                file_id = int(channel_object)
                # should be
                # base_file_obj = client.fetch_files_with_filter(path="/", filter_rules={"oc": {"fileid": file_id}}).data[0]
                # but it doesn't work...
                base_file_obj = [f for f in client.list_folders("/").data if f.file_id == file_id]
                if base_file_obj:
                    base_file_obj = base_file_obj[0]
            except ValueError:
                base_file_obj = client.get_file(channel_object)

            if not base_file_obj:
                raise FileNotFoundError(f"channel object not found: {channel_object}")

            files = client.list_folders(base_file_obj.get_relative_path(), depth=999).data

            # sanity check... needed
            files = [f for f in files if f.last_modified]

            # The last nb modification are at least the last nth modified file.
            # It could be less (3 times modification of the same file), but we can not
            # know.
            last_nth_modificated_files = sorted(
                files, key=lambda x: x.last_modified_datetime, reverse=True
            )[:nb]
            activities = []
            for f in last_nth_modificated_files:
                f_activities = client.get_activities(
                    object_type="files", object_id=f.file_id, **options
                )
                if f_activities.is_ok:
                    activities += f_activities.data
        else:
            # retrieve all activities
            activities = client.get_activities(**options).data

        contents = {}
        # TODO limit to nb last activities
        for activity in activities:
            activity["activity_id"] = str(activity["activity_id"])
            contents[activity["activity_id"]] = {
                **activity,
                "id": activity["activity_id"],
                "last_update_dt": now(),
                "creation_dt": activity["datetime"],
            }
        return contents
