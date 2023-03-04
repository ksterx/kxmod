import os
import platform
import tempfile
import time

import pyautogui as pag
import pywinctl as pwc

from kxmod.service.bot import SlackBot


def popup(app_name):
    window_list = pwc.getAllTitles()
    timeout = 10  # seconds
    freq = 0.1  # seconds
    while app_name not in window_list:
        time.sleep(freq)
        timeout -= freq
        if timeout < 0:
            raise ValueError("TIMEOUT: The app is not open. Try again after opening the app.")
        window_list = pwc.getAllTitles()

    for window in pwc.getAllTitles():
        if app_name == window:
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
    image_path = f"{tempfile.gettempdir()}/screenshot.png"
    screenshot(image_path)
    bot = SlackBot()
    bot.show("OTP", image_path)
    system = platform.system()
    if system == "Windows":
        return
    elif system == "Darwin":
        return
    elif system == "Linux":
        bot.say(get_ip())
    else:
        raise ValueError(f"Unknown system: {system}")


if __name__ == "__main__":
    main()
