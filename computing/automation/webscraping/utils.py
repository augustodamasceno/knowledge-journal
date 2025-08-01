#!/usr/bin/env python3
"""
This file is part of the Knowledge Journal
See https://github.com/augustodamasceno/knowledge-journal/
"""
__author__ = "Augusto Damasceno"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2025, Augusto Damasceno."
__license__ = "All rights reserved"

import random
import time
import os
import platform


def get_geckodriver_path():
    system = platform.system().lower()

    if system == "windows":
        paths = [
            r"C:\geckodriver\geckodriver.exe",
            r"C:\Program Files\geckodriver\geckodriver.exe",
            r"C:\webdrivers\geckodriver.exe"
        ]
    elif system == "darwin":
        paths = [
            "/usr/local/bin/geckodriver",
            "/opt/homebrew/bin/geckodriver",
            "/usr/bin/geckodriver"
        ]
    else:
        paths = [
            "/usr/local/bin/geckodriver",
            "/usr/bin/geckodriver",
            "/opt/geckodriver/geckodriver"
        ]

    for path in paths:
        if os.path.exists(path):
            return path

    return 'geckodriver'


def get_firefox_binary_path():
    system = platform.system().lower()

    if system == "windows":
        paths = [
            r"C:\Program Files\Mozilla Firefox\firefox.exe",
            r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
            os.path.expanduser(r"~\AppData\Local\Mozilla Firefox\firefox.exe")
        ]
    elif system == "darwin":  # macOS
        paths = [
            "/Applications/Firefox.app/Contents/MacOS/firefox",
            "/usr/local/bin/firefox"
        ]
    else:  # Linux/FreeBSD
        paths = [
            "/usr/bin/firefox",
            "/usr/local/bin/firefox",
            "/opt/firefox/firefox",
            "/snap/bin/firefox"
        ]

    for path in paths:
        if os.path.exists(path):
            return path

    return None


def type_like_human(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))