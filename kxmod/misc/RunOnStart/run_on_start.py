import os
import time

import pyautogui as pag
import pywinctl as pwc

from kxmod.service.bot import SlackBot


def popup(app_name):
    for window in pwc.getAllTitles():
        if app_name in window:
            win = pwc.getWindowsWithTitle(window)[0]
            win.activate()
        else:
            win = pwc.getWindowsWithTitle(window)[0]
            win.minimize()


def screenshot(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)
    popup("TeamViewer")
    time.sleep(0.5)
    pag.screenshot(image_path)


def get_ip():
    stream = os.popen('ip a | grep "inet 10"')
    ip = stream.read()
    return ip


def main():
    image_path = "/tmp/screenshot.png"
    screenshot(image_path)
    bot = SlackBot()
    bot.upload("OTP", image_path)
    bot.say(get_ip())


if __name__ == "__main__":
    main()
