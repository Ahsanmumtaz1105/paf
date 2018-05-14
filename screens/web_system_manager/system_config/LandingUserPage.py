import sys
import time
from robot.api.logger import error
from libs.utils.SeleniumUtil import SeleniumUtil
from libs.utils.CommonUtil import take_desktop_screenshot


class LandingUserPage:
    """
    """
    accounts_xpath = "//span[text()='Accounts']"
    users_xpath = "//span[text()='Users']"

    @staticmethod
    def open_users_page(driver):
        """
        """
        try:
            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, LandingUserPage.accounts_xpath, 30)
            driver.find_element_by_xpath(LandingUserPage.accounts_xpath).click()
            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, LandingUserPage.users_xpath, 30)
            driver.find_element_by_xpath(LandingUserPage.users_xpath).click()
            take_desktop_screenshot("open_user_success")
            time.sleep(1)
        except Exception as e:
            tb = sys.exc_info()[2]
            take_desktop_screenshot("Open_Users_Page_Failed")
            error("Exception in open_users_page. Details are - %s:: "
                  "Line Number[%s]" % (e.with_traceback(tb),
                                       sys.exc_info()[2].tb_lineno), True)
