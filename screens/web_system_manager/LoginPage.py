import socket
from libs.utils.SeleniumUtil import SeleniumUtil
from selenium.webdriver.common.by import By
from libs.utils.CommonUtil import take_desktop_screenshot
from libs.Drivers import *

user_name_textbox_id_locator = 'UserName'
password_textbox_id_locator = "Password"
login_button_xpath_locator = "//input[@class='eqButton']"
home_label_xpath_locator = "//span[text()='Home']"
login_username_xpath_locator = "//span[@id='HeaderUserInfoMenuUserName']"
login_non_admin_username_xpath_locator = \
    "//div[@id='Header']//div[@class='dropdown']/a/i[2]"


def login_to_equitrac_web_system_manager_as_admin(driver, user_name,
                                                  password, url=None):
    """
    Function Name -  login_to_equitrac_web_system_manager_as_admin
    Description - This method logins to web system manager as admin
    Parameters - driver, user_name, password, url=None
    Return -
    Author -  Dhananjay Joshi
    Modification date - 23-Apr-2018
    """
    try:

        if url is None:
            url = r"https://{}/EQWebClient".format(socket.gethostname())
        else:
            url = r"https://{}/EQWebClient".format(url)

        driver.get(url)
        SeleniumUtil.wait_for_an_element_to_be_present_by_id(
            driver, user_name_textbox_id_locator, 30)
        usr_name_object = driver.find_element(
            By.ID, user_name_textbox_id_locator)
        usr_name_object.click()
        usr_name_object.clear()
        usr_name_object.send_keys(user_name)
        password_object = driver.find_element(
            By.ID, password_textbox_id_locator)
        password_object.click()
        password_object.clear()
        password_object.send_keys(password)

        # Click on submit button
        driver.find_element(By.XPATH, login_button_xpath_locator).click()
        SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
            driver, login_username_xpath_locator, 30)
        user_name = driver.find_element(
            By.XPATH, login_username_xpath_locator).text
        take_desktop_screenshot("Login_to_Equitrac")
        info("Logged in with User %s" % user_name, True, True)
    except Exception as e:
        tb = sys.exc_info()[2]
        take_desktop_screenshot("Login_to_Equitrac_Failed")
        error("Exception in login_to_equitrac. Details are - %s:: Line "
              "Number[%s]" % (e.with_traceback(tb),
                              sys.exc_info()[2].tb_lineno), True)
        raise Exception("Login to equitrac web system manager "
                        "admin user failed")


def login_to_equitrac_web_system_manager_as_non_admin(driver, user_name,
                                                      password, url=None):
    """
    Function Name -  login_to_equitrac_web_system_manager_as_non_admin
    Description - This method logins to web system manager as non admin
    Parameters - driver, user_name, password, url=None
    Return -
    Author -  Dhananjay Joshi
    Modification date - 23-Apr-2018
    """
    try:

        if url is None:
            url = r"https://{}/EQWebClient".format(socket.gethostname())
        else:
            url = r"https://{}/EQWebClient".format(url)

        driver.get(url)
        SeleniumUtil.wait_for_an_element_to_be_present_by_id(
            driver, user_name_textbox_id_locator, 30)
        usr_name_object = driver.find_element(
            By.ID, user_name_textbox_id_locator)
        usr_name_object.click()
        usr_name_object.clear()
        usr_name_object.send_keys(user_name)
        password_object = driver.find_element(
            By.ID, password_textbox_id_locator)
        password_object.click()
        password_object.clear()
        password_object.send_keys(password)
        # Click on submit button
        driver.find_element(By.XPATH, login_button_xpath_locator).click()
        SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
            driver, login_username_xpath_locator, 30)
        user_name = driver.find_element(
            By.XPATH, login_non_admin_username_xpath_locator).text
        take_desktop_screenshot("Login_to_Equitrac")
        info("Logged in with User <b>%s </b>" % user_name, True, True)
    except Exception as e:
        tb = sys.exc_info()[2]
        error("Exception in common>> "
              "login_to_equitrac_web_system_manager_as_non_admin. Details are "
              "- [%s]::Line Number[%s]" % (e.with_traceback(tb),
                                           sys.exc_info()[2].tb_lineno), True)
        raise Exception("Exception occurred in "
                        "login_to_equitrac_web_system_manager_as_non_admin ")