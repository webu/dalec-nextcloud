# ☁ dalec-nextcloud

[![Stable Version](https://img.shields.io/pypi/v/dalec-nextcloud?color=blue)](https://pypi.org/project/dalec-nextcloud/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![semver](https://img.shields.io/badge/semver-2.0.0-green)](https://semver.org/)

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


