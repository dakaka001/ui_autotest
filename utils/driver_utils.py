import os

from selenium import webdriver

class DriverUtils():

    @staticmethod
    def get_driver():
        execute_path = os.path.dirname(os.getcwd()) + "/chromedriver.exe"
        driver = webdriver.Chrome(execute_path)

        return driver