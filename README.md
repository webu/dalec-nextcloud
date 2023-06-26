# ☁ dalec-nextcloud

Django Aggregate a Lot of External Content -- Nextcloud

Aggregate last nextcloud files activity from a given nextcloud instance.

Plugin of [🤖 dalec](https://github.com/webu/dalec).

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

### Activity

Retrieves latest activities.

 - If `channel` is `"files"`, retrieve only for this file or directory.
 - If `channel` is `"files_and_childs"`, retrieve recursively from this folder and child.
 - If `channel` is `None`, retrieve all activities.

`channel_object` is the nextcloud `file_id`.

```django
{% dalec "nexctloud" "activity" %}
{% dalec "nexctloud" "activity" channel="files" channel_object="55145"%}
{% dalec "nexctloud" "activity" channel="files_and_childs" channel_object="55145"%}
```


## Settings

Django settings must define:

  - `DALEC_NEXTCLOUD_BASE_URL` : nextcloud instance url (ex: `https://nextcloud.org/`)
  - `DALEC_NEXTCLOUD_API_USERNAME` : nextcloud username (ex: `admin`)
  - `DALEC_NEXTCLOUD_API_PASSWORD` : nextcloud user password (ex: `azeazeaezdfqsmlkrjzr`)


