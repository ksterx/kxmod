import json

import requests

from . import my_config


def line_notify(message):
    token = my_config.LINE_TOKEN
    api = 'https://notify-api.line.me/api/notify'

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + token}
    requests.post(api, data=payload, headers=headers)


def slack_notify(message, usr='Python'):
    web_hook_url = my_config.SLACK_URL
    requests.post(web_hook_url, data=json.dumps({
        'text': message,
        'username': usr,
        'link_names': 1
    }))
