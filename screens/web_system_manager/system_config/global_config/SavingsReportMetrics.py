import time
import xmltodict
from selenium.webdriver.common.by import By
from libs.utils.DatabaseOperations import *

page_title_class_locator = "nu-title-text"
system_configuration_xpath_locator = "//span[text()='System Configuration']"
global_configuration_settings_xpath_locator = "//span[text()=" \
                                              "'Global Configuration Settings']"
user_interaction_xpath_locator = "//h4[text()='User Interaction']"
saving_report_metrics_xpath_locator = "//h4[text()='Savings Report Metrics']"
measurement_system_class_locator = "caret"
one_tree_is_equivalent_to_xpath_locator = \
    "//div[text()='One tree is equivalent to']//..//..//..//input"
one_page_is_equivalent_to_xpath_locator = \
    "//div[text()='One Letter/A4 page uses']//..//..//..//input"
one_kg_paper_is_equivalent_to_xpath_locator = \
    "//div[text()='One kg of paper releases']//..//..//..//input"
apply_button_xpath_locator = "//span[text()='Apply']"
status_message_class_locator= \
    ".eq-alert.alert.alert-dismissible.alert-success.fade.in.nu-alert"


def navigate_to_savings_report_metrics_page(driver):
    """
    Function Name -  navigate_to_savings_report_metrics_page
    Description - This method navigates to savings report metrics page
    Parameters - driver
    Return - driver
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    try:
        # Click on system configuration link
        driver.find_element_by_xpath(
            system_configuration_xpath_locator).click()
        time.sleep(7)

        # Click on global configuration settings link
        driver.find_element_by_xpath(
            global_configuration_settings_xpath_locator).click()
        time.sleep(7)

        # Click on user interaction link
        driver.find_element_by_xpath(user_interaction_xpath_locator).click()
        time.sleep(7)

        # Click on savings report metrics
        driver.find_element_by_xpath(saving_report_metrics_xpath_locator).\
            click()
        time.sleep(10)

        # Verify navigation is successful to Savings report metrics page
        title = get_page_title(driver)
        title_verification_result = verify_savings_report_metrics_page_title(
            title)
        if title_verification_result is True:
            print("Successfully navigated to Savings Report Metrics Page")
        else:
            error("Failed to navigate to Savings Report Metrics Page")
        return driver
    except Exception as e:
        tb = sys.exc_info()[2]
        error(
            "Exception in common>> navigateToSavingsReportMetricsPage. "
            "Details are - [%s]::Line Number[%s]" % (
                e.with_traceback(tb), sys.exc_info()[2].tb_lineno), True)
        raise Exception(
            "Exception occurred in navigateToSavingsReportMetricsPage ")


def get_page_title(driver):
    """
    Function Name -  getPageTitle
    Description - This method Returns the title of page
    Parameters - driver
    Return - Page title
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    time.sleep(2)
    title = driver.find_element(
        By.CLASS_NAME, page_title_class_locator).\
        text.strip()
    print(title)
    return title


def verify_savings_report_metrics_page_title(actual_title):
    """
    Function Name -  verifySavingsReportMetricsPageTitle
    Description - Verifies the title of Savings Report Metric page
    Parameters - Page title
    Return - Page title comparison result
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    result = False
    if actual_title == "Savings Report Metrics":
        result = True
    return result


def select_measurement_system(driver, option):
    """
    Function Name -  selectMeasurementSystem
    Description - Selects the measurement system from drop down
    Parameters - driver, option to select
    Return - None
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    driver.find_element_by_class_name(measurement_system_class_locator).click()
    list_element = driver.find_elements_by_xpath(
        ".//ul/li/ul[@class='nu-scrollable-menu"
        " dropdown-menu']/li")
    for item in list_element:
        text_value = item.find_element_by_tag_name("span").text
        if option == text_value:
            item.find_element_by_tag_name('a').click()
            time.sleep(2)


def set_one_tree_is_equivalent_to_value(driver, value_to_set):
    """
    Function Name -  setOneTreeIsEquivalentToValue
    Description - Sets one tree is equivalent textbox value
    Parameters - driver, value to set
    Return - None
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    driver.find_element(By.XPATH, one_tree_is_equivalent_to_xpath_locator).\
        clear()
    driver.find_element(By.XPATH, one_tree_is_equivalent_to_xpath_locator).\
        send_keys(value_to_set)
    time.sleep(2)


def set_one_page_uses_to_value(driver, value_to_set):
    """
    Function Name -  setOnePageUsesToValue
    Description - Sets one page uses to textbox value
    Parameters - driver, value to set
    Return - None
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    driver.find_element(By.XPATH, one_page_is_equivalent_to_xpath_locator).\
        clear()
    driver.find_element(By.XPATH, one_page_is_equivalent_to_xpath_locator).\
        send_keys(
        value_to_set)
    time.sleep(2)


def set_one_kg_of_paper_release_to_value(driver, value_to_set):
    """
    Function Name -  setOneKGOfPaperReleaseToValue
    Description - Sets one KG of paper uses to textbox value
    Parameters - driver, value to set
    Return - None
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    driver.find_element(By.XPATH, one_kg_paper_is_equivalent_to_xpath_locator).\
        clear()
    driver.find_element(By.XPATH, one_kg_paper_is_equivalent_to_xpath_locator).\
        send_keys(
        value_to_set)
    time.sleep(2)


def save_changes_to_report_metrics(driver):
    """
    Function Name -  saveChangesToReportMetrics
    Description - Saves the changes on savings report metrics page and
    verifies save successful message
    Parameters - driver
    Return - None
    Author -  Amol Chitte
    Modification date - 23-Apr-2018
    """
    driver.find_element(By.XPATH, apply_button_xpath_locator).click()
    time.sleep(2)
    status_message = driver.find_element(By.CSS_SELECTOR,
                                         status_message_class_locator).text
    expected_status_message = "The requested operation has been " \
                              "submitted and successfully completed"
    if status_message.find(expected_status_message) == -1:
        error("Failed to verify operation completed status message")
    else:
        print("Successfully verified operation completed status message")
    time.sleep(2)


def verify_savings_report_metrics_values_in_database(measurement_system,
                                                     one_tree_equivalent,
                                                     one_page_uses,
                                                     one_kg_of_paper):
    """
    Function Name -  verifySavingsReportMetricsValuesInDatabase
    Description - Verifies the savings report metrics parameter values are
    reflected in database table
    Parameters - measurement_system, one_tree_equivalent,
    one_page_uses, one_kg_of_paper
    Return - None
    Author -  Amol Chitte
    Modification date - 24-Apr-2018
    """
    try:
        expected_updated_value = [str(one_tree_equivalent),
                                  str(one_page_uses), str(one_kg_of_paper)]
        sql_query = "SELECT attrvalue FROM cas_config where attribute " \
                    "='SavingsReportConfig'"

        # Execute the query
        db_result = sql(sql_query)

        # Fetch and parse the result
        result = db_result.fetchall()
        data = xmltodict.parse(result[0][0])

        # Compare the expected and actual data
        db_data = data.get('SR_Config', 'SR_Config')
        if db_data['System'] != measurement_system:
            raise AssertionError('Not {} measurement'.format
                                 (measurement_system))
        else:
            print("Correct measurement")
        del db_data['System']
        act_db_value = [val for val in db_data.values()]
        result = compare_list(expected_updated_value, act_db_value)
        if result is not True:
            raise AssertionError("Failed to verify savings report metrics "
                                 "values are updated in database")
        else:
            print("Successfully verified savings report metrics values "
                  "are updated in database")
    except Exception as e:
        tb = sys.exc_info()[2]
        error(
            "Exception in common>> "
            "verifySavingsReportMetricsValuesInDatabase"
            ". Details are - [%s]::Line Number[%s]" % (
                e.with_traceback(tb), sys.exc_info()[2].tb_lineno), True)
        raise Exception("Exception occurred in "
                        "verifySavingsReportMetricsValuesInDatabase")