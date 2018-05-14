import time
import sys
from libs.utils.SeleniumUtil import SeleniumUtil
from robot.api.logger import error
from robot.api.logger import info
from libs.utils.CommonUtil import take_desktop_screenshot


class Users:
    """
    Class Name -  Users
    Description - This class contains user creation related common
    methods used in framework
    development
    Parameters - None
    Return - None
    Author -  Dhananjay Joshi
    Modification date - 17-Apr-2018
    """

    @staticmethod
    def create_users_details(driver, user_id, user_name, email):
        """
        Function Name -  create_users_details
        Description - This method creates user details
        Parameters - driver, user_id, user_name, email
        Return -
        Author -  Dhananjay Joshi
        Modification date - 03-May-2018
        """
        try:

            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, "//iframe[@class='nu-iframe']", 30)

            driver.switch_to.frame(
                driver.find_element_by_xpath("//iframe[@class='nu-iframe']"))
            take_desktop_screenshot("Add_User_Page")
            time.sleep(5)
            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, "//a[@id='AddUserButton']", 30)
            driver.find_element_by_xpath("//a[@id='AddUserButton']").click()
            time.sleep(2)
            driver.switch_to.default_content()
            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, "//iframe[@class='nu-iframe']", 20)

            driver.switch_to.frame(
                driver.find_element_by_xpath("//iframe[@class='nu-iframe']"))
            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, "//input[@id='Name']", 20)
            driver.find_element_by_xpath("//input[@id='Name']").send_keys(
                user_id)
            driver.find_element_by_xpath("//input[@id='FullName']").send_keys(
                user_name)
            driver.find_element_by_xpath(
                "//input[@id='EmailAddress']").send_keys(email)
            take_desktop_screenshot("Adding_Users")
            driver.find_element_by_xpath("//input[@id='SaveButton1']").click()
            time.sleep(2)

        except Exception as e:
            tb = sys.exc_info()[2]
            take_desktop_screenshot("create_users_details_error")
            error("Exception in create_users_details. Details are - "
                  "%s:: Line Number[%s]" % (e.with_traceback(tb),
                                            sys.exc_info()[2].tb_lineno), True)

    @staticmethod
    def get_users_detail(driver, user_id):
        """
        Function Name -  get_users_detail
        Description - This method creates user details
        Parameters - driver, user_id
        Return -
        Author -  Dhananjay Joshi
        Modification date - 03-May-2018
        """
        dict_user_info = {}
        try:
            time.sleep(10)
            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, "//iframe[@class='nu-iframe']", 20)
            time.sleep(1)
            driver.switch_to.frame(
                driver.find_element_by_xpath("//iframe[@class='nu-iframe']"))
            time.sleep(1)
            take_desktop_screenshot("get_user_details")
            all_users = driver.find_elements_by_xpath(
                "//table[@id='ItemList']//tr")

            j = 3
            for user in range(len(all_users)):
                temp = "//table[@id='ItemList']//tr[" + str(j) + "]//td[2]//a"
                user_name = driver.find_element_by_xpath(temp).\
                    get_attribute("text")

                if user_name.lower() == user_id.lower():
                    temp2 = "//table[@id='ItemList']//tr[" + str(
                        j) + "]//td[2]//a"
                    SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                        driver, temp2, 20)
                    driver.find_element_by_xpath(temp2).click()
                    break
                j = j + 1

            time.sleep(1)
            driver.switch_to.default_content()
            SeleniumUtil.wait_for_an_element_to_be_present_by_xpath(
                driver, "//iframe[@class='nu-iframe']", 30)
            driver.switch_to.frame(
                driver.find_element_by_xpath("//iframe[@class='nu-iframe']"))
            time.sleep(5)
            take_desktop_screenshot("get_user_details")
            primary_pin = driver.find_element_by_xpath(
                "//input[@id='PrimaryPin']").get_attribute("value")

            secondary_pin = driver.find_element_by_xpath(
                "//input[@id='SecondaryPin']").get_attribute("value")

            alternate_pin = driver.find_element_by_xpath(
                "//input[@id='AlternatePrimaryPin']").get_attribute("value")

            home_print_server = driver.find_element_by_xpath(
                "//input[@id='HomeServer']").get_attribute("value")

            home_drive = driver.find_element_by_xpath(
                "//input[@id='HomeFolder']").get_attribute("value")

            department = driver.find_element_by_xpath(
                "//input[@id='DepartmentId']/ancestor::*[1]/div/input").\
                get_attribute("value")

            location = driver.find_element_by_xpath(
                "//form[@id='UserProperties']/div/div/div[2]/table/tbody/tr[9]"
                "/td[2]/div/input").get_attribute("value")

            email = driver.find_element_by_xpath(
                "//input[@id='EmailAddress']").get_attribute("value")
            full_name = driver.find_element_by_xpath(
                "//input[@id='FullName']").get_attribute("value")
            balance = driver.find_element_by_xpath(
                "//input[@id='Balance']").get_attribute("value")
            default_billing_code = driver.find_element_by_xpath(
                "//input[@id='DefaultBillingCodeId']/ancestor::*[1]/div/input"
                "").get_attribute("value")
            minimum_balance = driver.find_element_by_xpath(
                "//input[@id='MinimumBalance']").get_attribute("value")
            try:
                color_quota_total_pages = driver.find_element_by_xpath(
                    "//input[@id='ColorQuota']").get_attribute("value")
                color_quota_page_usage = driver.find_element_by_xpath(
                    "//input[@id='PageUsage']").get_attribute("value")
                color_quota_remaining_pages = driver.find_element_by_xpath(
                    "//input[@id='RemainingPages']").get_attribute("value")
            except BaseException as e:
                info("Exception is ", repr(e))
                color_quota_total_pages = "disabled"
                color_quota_page_usage = "disabled"
                color_quota_remaining_pages = "disabled"
                pass
            driver.switch_to.default_content()
            dict_user_info["primaryPIN"] = primary_pin
            dict_user_info["sencondaryPIN"] = secondary_pin
            dict_user_info["alternatePIN"] = alternate_pin
            dict_user_info["homePrintServer"] = home_print_server
            dict_user_info["FullName"] = full_name
            dict_user_info["email"] = email
            dict_user_info["homeDrive"] = home_drive
            dict_user_info["Balance"] = balance
            dict_user_info["department"] = department
            dict_user_info["location"] = location
            dict_user_info["minimum_balance"] = minimum_balance
            dict_user_info["default_billing_code"] = default_billing_code
            try:
                dict_user_info["colorquota_totalpages"] = \
                    color_quota_total_pages
                dict_user_info["colorquota_PageUsage"] = \
                    color_quota_page_usage
                dict_user_info["colorquota_RemainingPages"] = \
                    color_quota_remaining_pages
            except BaseException as e:
                info("Exception is ", repr(e))
                pass
            info("User details fetched are:: %s" % dict_user_info)

        except Exception as e:

            tb = sys.exc_info()[2]
            info("User details fetched are:: %s" % dict_user_info)
            error("Exception in get_user_detail. Details are - %s:: "
                  "Line Number[%s]" % (e.with_traceback(tb),
                                       sys.exc_info()[2].tb_lineno), True)

        return dict_user_info

    @staticmethod
    def log_out(driver):
        """
        Function Name -  log_out
        Description - This method perofrms log out operation
        Parameters - driver
        Return -
        Author -  Dhananjay Joshi
        Modification date - 03-May-2018
        """
        try:
            # Logout from application
            time.sleep(5)
            driver.find_element_by_css_selector("i.fa.fa-angle-down").click()
            time.sleep(2)
            driver.find_element_by_xpath("//a[contains(text(),'Logoff')]").\
                click()
            time.sleep(5)
            info("Log out success", True, True)

        except Exception as e:
            tb = sys.exc_info()[2]
            error("Exception in logout. Details are - %s:: Line Number[%s]" % (
                e.with_traceback(tb), sys.exc_info()[2].tb_lineno), True)
            raise Exception("Exception occurred while logging out")
        return driver