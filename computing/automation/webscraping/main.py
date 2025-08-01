#!/usr/bin/env python3
"""
This file is part of the Knowledge Journal
See https://github.com/augustodamasceno/knowledge-journal/
"""
__author__ = "Augusto Damasceno"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2025, Augusto Damasceno."
__license__ = "All rights reserved"


import platform
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import utils


class IMDBScraping:
    def __init__(self):
        self.main_page = 'https://imdb.com/pt'
        try:
            gecko_driver = utils.get_geckodriver_path()
            self.service = Service(executable_path=gecko_driver)
        except Exception as e:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            print(f"Error initializing geckodriver service: {e}\n"
                   + "Please ensure geckodriver is installed and the path is correct.\n"
                   + r"You can download it from https://github.com/mozilla/geckodriver/releases"
                   + "\n  and place it in " + r"C:\Program Files\geckodriver"
                   + f"\n  or {current_folder}")
            self.service = None

        try:
            options = Options()
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
            options.set_preference("general.useragent.override", user_agent)
            options.set_preference("dom.webdriver.enabled", False)
            options.set_preference('useAutomationExtension', False)
            options.set_preference("intl.accept_languages", "pt-BR, pt")
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("geo.enabled", False)
            options.add_argument("--start-maximized")
            firefox_binary = utils.get_firefox_binary_path()
            if firefox_binary:
                options.binary_location = firefox_binary
            else:
                print("Warning: Firefox binary not found in default locations")
            self.driver = webdriver.Firefox(service=self.service, options=options)
        except Exception as e:
            print(f"Error initializing Firefox driver: {e}")
            self.driver = None
        self.logged = False

    def login(self, user, password):
        try:
            self.driver.get(self.main_page)
            wait = WebDriverWait(self.driver, 3)

            xpath_login_button = "//a[.//span[text()='Fazer login']]"
            wait = WebDriverWait(self.driver, 5)
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath_login_button))
            )
            login_button.click()
            time.sleep(2)

            xpath_login_button2 = "//a[.//span[text()='Faça login com o IMDb']]"
            wait = WebDriverWait(self.driver, 5)
            login_button2 = wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath_login_button2))
            )
            login_button2.click()
            time.sleep(2)

            email_field = wait.until(EC.visibility_of_element_located((By.ID, "ap_email")))
            utils.type_like_human(email_field, user)

            password_field = self.driver.find_element(By.ID, "ap_password")
            utils.type_like_human(password_field, password)

            signin_button = self.driver.find_element(By.ID, "signInSubmit")
            signin_button.click()

            self.logged = True
        except Exception as e:
            self.logged = False
            print("Error interacting with the page:", e)


    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    bot = IMDBScraping()
    bot.login(user="user", password='password')