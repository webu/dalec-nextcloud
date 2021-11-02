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
            return self._fetch_activiy(nb, channel, channel_object)

        raise ValueError(f"Invalid content_type {content_type}. Accepted: topic, category." )

    def _fetch_activity(self, nb, channel=None, channel_object=None):
        """
        Get latest activities from entire nextcloud or channel
        """
        options = {
                "per_page": nb,
                }

        activities = client.get_activities(
                channel_type=channel,
                channel_id=channel_object,
                **options
                ).data


        contents = {}
        for activity in activities:
            contents[activity["activity_id"]] = {
                    **activity,
                    "last_update_dt": now(),
                    "creation_dt": activity["datetime"]
                    }
        return contents

