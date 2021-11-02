# dalec-nextcloud

Django Aggregate a Lot of External Content -- Nextcloud

Aggregate last discourse issue or event from a given nextcloud instance.

Plugin of [dalec](https://dev.webu.coop/w/i/dalec).

## Installation

```
pip install dalec_nextcloud
```

In django settings `INSTALLED_APPS`, add:

```
INSTALLED_APPS = [
    ...
    "dalec",
    "dalec_prime",
    "dalec_nextcloud",
    ...
    ]
```


## Usage

General usage:
```django
{% load dalec %}

{% dalec "nextcloud" content_type [channel=None] [channel_object=None] [template=None] %}
```

Real examples:

### Topics

Retrieves latest activities:
```django
{% dalec "discourse" "activity" %}
```


## Settings

Django settings must define:

  - `DALEC_NEXTCLOUD_BASE_URL` : nextcloud instance url (ex: `https://nextcloud.org/`)
  - `DALEC_NEXTCLOUD_API_USERNAME` : nextcloud username (ex: `admin`)
  - `DALEC_NEXTCLOUD_API_PASSWORD` : nextcloud user password (ex: `azeazeaezdfqsmlkrjzr`)


