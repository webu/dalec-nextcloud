# Content returned by dalec_nextcloud

Every dalec save in database object with the following attributes:

 - `last_update_dt` 
 - `creation_dt` 
 - `app` 
 - `content_type` 
 - `channel` 
 - `channel_object` 
 - `dj_channel_content_type_id`
 - `dj_channel_id`
 - `dj_content_content_type_id`
 - `dj_content_id`
 - `content_id`
 - `content_data`

See [the main dalec](https://github.com/webu/dalec) repository for more information.
Hereafter are detailed the `content_data`, specific to the `nexctloud` content type.

## Activity

```json
{'id': '532033',
 'app': 'files',
 'icon': 'https://cloud.dalec.org/apps/files/img/add-color.svg',
 'link': 'https://cloud.dalec.org/index.php/apps/files/?dir=/To-the-moon/Just%20send%20it',
 'type': 'file_created',
 'user': 'stck_dalec',
 'message': '',
 'objects': {'88823': '/To-the-moon/Just send it/Readme.md'},
 'subject': 'Created by dalec',
 'datetime': '2023-04-26T00:08:19+00:00',
 'object_id': 88823,
 'activity_id': '532033',
 'creation_dt': '2023-04-26T00:08:19+00:00',
 'object_name': '/To-the-moon/Just send it/Readme.md',
 'object_type': 'files',
 'message_rich': ['', []],
 'subject_rich': [
    'Created by {user}',
    {
      'file': {
        'id': '42',
        'link': 'https://cloud.dalec.org/index.php/f/666',
        'name': 'Readme.md',
        'path': 'To-the-moon/Just send it/Readme.md',
        'type': 'file'
      },
      'user': {'id': 'stck_dalec', 'name': 'dalec', 'type': 'user'}
    }
  ],
 'last_update_dt': '2023-05-05T08:40:26.833Z'}
```
