import json
import os
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
        with open(f"{os.path.dirname(__file__)}/credentials.yaml") as f:
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

    def say(self, message, image_path=None):
        token = self.credentials["LINE_TOKEN"]
        payload = {"message": message}
        headers = {"Authorization": "Bearer " + token}
        if image_path is not None:
            files = {"imageFile": open(image_path, "rb")}
        else:
            files = None
        requests.post(self.API, data=payload, headers=headers, files=files)


class SlackBot(Bot):
    def __init__(self):
        super().__init__("slack")

    def say(self, message):
        url = "https://slack.com/api/chat.postMessage"
        data = {
            "token": self.credentials["SLACK_BOT_TOKEN"],
            "channel": self.credentials["SLACK_BOT_CHANNEL"],
            "text": message,
        }
        requests.post(url, data=data)

    def upload(self, message: str, file_path: str):
        url = "https://slack.com/api/files.upload"
        data = {
            "token": self.credentials["SLACK_BOT_TOKEN"],
            "channels": self.credentials["SLACK_BOT_CHANNEL"],
            "initial_comment": message,
        }
        files = {"file": open(file_path, "rb")}
        requests.post(url, data=data, files=files)
