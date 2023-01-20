import json
import os

import requests


def line(message: str):
    """Notify message by using LINE.

    Args:
        message (str): Displayed message in your LINE chatroom.
    """
    token = "FkhhJG7A4yZmawTo09qPv27sGCcEXWzU1tr03t4xsyJ"
    api = "https://notify-api.line.me/api/notify"

    payload = {"message": message}
    headers = {"Authorization": "Bearer " + token}
    requests.post(api, data=payload, headers=headers)


def slack(message: str, botname="CodeBot"):
    """Notify message by using Slack.

    Args:
        message (str): Dispayed message in your workspace
        botname (str, optional): Displayed botname in your workspace. Defaults to 'Python'.
    """

    if ("SLACK_WEBHOOK_URL" in os.environ) is False:
        raise Exception(
            "No 'SLACK_WEBHOOK_URL' found in your environment variables."
            "Set a variable with 'export 'SLACK_WEBHOOK_URL' on your terminal."
            "See 'https://api.slack.com/messaging/webhooks'."
        )

    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
    requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps({"text": message, "username": botname, "link_names": 1}),
    )
