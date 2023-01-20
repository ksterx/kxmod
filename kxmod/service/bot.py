import json
from abc import ABC, abstractmethod

import requests
import yaml


class Bot(ABC):
    def __init__(self, messenger):
        """
        notifier = Notifier(["line", "slack"])
        notifier.notify("Hello")
        """

        self.messenger = messenger
        with open("credentials.yaml") as f:
            self.credentials = yaml.safe_load(f)

    @abstractmethod
    def say(self, message):
        pass

    def monitor(self, func):
        def wrapper(*args, **kwargs):
            message = func(*args, **kwargs)
            self.say(message)
            return message

        return wrapper


class LineBot(Bot):
    API = "https://notify-api.line.me/api/notify"

    def __init__(self):
        super().__init__("line")

    def say(self, message):
        token = self.credentials["LINE_TOKEN"]
        payload = {"message": message}
        headers = {"Authorization": "Bearer " + token}
        requests.post(self.API, data=payload, headers=headers)


class SlackBot(Bot):
    def __init__(self):
        super().__init__("slack")

    def say(self, message):
        webhook = self.credentials["SLACK_WEBHOOK_URL"]
        requests.post(webhook, json.dumps({"text": message}))
