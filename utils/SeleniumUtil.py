import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from robot.api.logger import info


class SeleniumUtil:
    """
    Class Name -  SeleniumUtil
    Description - This class contains some common wait methods used in framework
    development
    Parameters - None
    Return - None
    Author -  Dhananjay Joshi
    Modification date - 17-Apr-2018
    """
    @staticmethod
    def wait_for_an_element_to_be_present_by_xpath(driver, element_xpath,
                                                   time_out_in_seconds=30):
        """
        Function Name -  wait_for_an_element_to_be_present_by_xpath
        Description - Dynamic wait by xpath
        Parameters - driver, element_xpath,time_out_in_seconds=30
        Return - None
        Author -  Dhananjay Joshi
        Modification date - 24-Apr-2018
        """
        try:
            WebDriverWait(driver, int(time_out_in_seconds)).until(
                ec.visibility_of_element_located((By.XPATH, element_xpath)))
            WebDriverWait(driver, int(time_out_in_seconds)).until(
                ec.presence_of_element_located((By.XPATH, element_xpath)))
            print("element found")
        except Exception as e:
            tb = sys.exc_info()[2]
            info("Exception in reading excel data in "
                 "def wait_for_an_element_to_be_present_by_xpath as  [%s]:: "
                 "Line Number[%s]" % (e.with_traceback(tb),
                                      sys.exc_info()[2].tb_lineno), True)

    @staticmethod
    def wait_for_an_element_to_be_present_by_id(
            driver, element_xpath, time_out_in_seconds=30):
        """
        Function Name -  wait_for_an_element_to_be_present_by_id
        Description -Dynamic wait by Id
        Parameters - driver, element_xpath, time_out_in_seconds=30
        Return - None
        Author -  Dhananjay Joshi
        Modification date - 24-Apr-2018
        """

        try:
            WebDriverWait(driver, int(time_out_in_seconds)).\
                until(ec.visibility_of_element_located((By.ID, element_xpath)))
            WebDriverWait(
                driver, int(time_out_in_seconds)).until(
                ec.presence_of_element_located((By.ID, element_xpath)))
        except Exception as e:
            tb = sys.exc_info()[2]
            info("Exception in reading excel data in "
                 "def wait_for_an_element_to_be_present_by_id as  [%s]:: "
                 "Line Number[%s]" % (e.with_traceback(tb),
                                      sys.exc_info()[2].tb_lineno), True)