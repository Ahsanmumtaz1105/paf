import os
import sys
import time
from robot.api.logger import *
from selenium import webdriver
from libs.utils.CommonUtil import get_project_path


class Drivers:
    """
    """
    driver = None

    @staticmethod
    def get_selenium_web_driver_instance(browser_type="chrome"):
        """
        """
        try:
            if Drivers.driver is None:
                # Chrome web driver instantiation
                if browser_type.lower() == 'chrome':
                    Drivers.driver = webdriver.Chrome(
                        str(get_project_path()) + "\\libs\\chromedriver.exe")
                    Drivers.driver.maximize_window()
                # IE web driver instantiation
                elif browser_type.lower() == 'ie':
                    Drivers.driver = webdriver.Ie()
                # Firefox web driver instantiation
                elif browser_type.lower() == 'firefox':
                    Drivers.driver = webdriver.Firefox()
                else:
                    error("Invalid Input for Browser type - %s" % browser_type)

            return Drivers.driver
        except Exception as e:
            tb = sys.exc_info()[2]
            error("Exception in Drivers>>get_selenium_web_driver_instance. "
                  "Details are - [%s]::Line Number[%s]" % (e.with_traceback(tb),
                                                           sys.exc_info()[2].
                                                           tb_lineno), True)
            raise Exception("Exception occurred in api_login ")

    @staticmethod
    def close_driver():
        """
        """
        try:
            Drivers.driver.close()
        except Exception as e:
            tb = sys.exc_info()[2]
            error("Exception in Drivers>>close_driver. Details are - "
                  "[%s]::Line Number[%s]" % (e.with_traceback(tb),
                                             sys.exc_info()[2].tb_lineno), True)

    @staticmethod
    def start_winium_driver():
        """
        """
        try:

            info("starting winium driver...", True, True)
            winium_driver = webdriver.Remote(
                command_executor='http://localhost:9999',
                desired_capabilities={
                    "debugConnectToRunningApp": 'false',
                    "app": r"C:/windows/system32/calc.exe"
                })

            info("winium driver has started successfully...", True, True)
            time.sleep(2)
            os.system("TASKKILL /F /IM Calculator.exe")
            os.system("TASKKILL /F /IM Calc.exe")
            os.system("TASKKILL /F /IM win32calc.exe")
            return winium_driver

        except Exception as e:
            os.system("TASKKILL /F /IM Calculator.exe")
            os.system("TASKKILL /F /IM win32calc.exe")
            os.system("TASKKILL /F /IM Calc.exe")
            tb = sys.exc_info()[2]
            error("Exception thrown in starting winium driver as. Details are -"
                  "[%s]::Line Number[%s]" % (e.with_traceback(tb),
                                             sys.exc_info()[2].tb_lineno), True)
            raise Exception("Unable to start winium desktop driver")
