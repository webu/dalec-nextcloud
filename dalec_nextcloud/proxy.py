from datetime import timedelta
from typing import Dict
import requests

from django.utils.dateparse import parse_datetime
from django.utils.timezone import now
from django.conf import settings

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

        raise ValueError(f"Invalid content_type {content_type}. Accepted: topic, category." )

    def _fetch_activity_file(self, nb, channel=None, channel_object=None):
        """
        Get latest activities from entire nextcloud or channel
        """
        options = {
                "limit": nb,
                }

        if channel:
            if channel not in ["files"]:
                raise ValueError(
                    """Value `{}` is not a correct value for channel type and Activity.
                    It must be either "files" or None.
                    """.format(
                        channel
                    )
                )
            if not channel_object:
                raise ValueError(
                        """channel_object must be provided together with channel"""
                        )
        elif channel_object:
            raise ValueError("channel must be provided together with channel_object")

        def _list_rec(d, files):
            # list files recursively
            files.append(d)
            if d.isdir():
                for i in d.list():
                    _list_rec(i, files=files)

        # get base path
        if channel == "files":
            base_file = client.get_activities(
                    object_type="files",
                    object_id=channel_object
                    ).data[0]["object_name"]
            
            base_file_obj= client.get_file(base_file)
            files = []
            _list_rec(base_file_obj, files)

            activities = []
            for f in files:
                f_activities = client.get_activities(
                            object_type="files",
                            object_id=f.file_id,
                            **options
                            )
                if f_activities.is_ok:
                    activities += f_activities.data

        else:
            activities = client.get_activities(
                    **options,
                    ).data

        contents = {}
        for activity in activities:
            contents[str(activity["activity_id"])] = {
                    **activity,
                    "id": activity["activity_id"],
                    "last_update_dt": now(),
                    "creation_dt": activity["datetime"]
                    }
        return contents

