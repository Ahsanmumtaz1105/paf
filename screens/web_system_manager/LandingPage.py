def get_user_name(driver):
    """
    Function Name -  get_user_name
    Description - This method gets user name
    Parameters - driver
    Return - driver
    Author -  Dhananjay Joshi
    Modification date - 23-Apr-2018
    """
    with driver.wait(15):
        display_user_name = driver.find_element_by_xpath(
            "//div[""@id='UserDisplayName']").text
        user_name = display_user_name.split("\\")
    return user_name[1]


def get_location(driver):
    """
    Function Name -  get_location
    Description - This method gets location
    Parameters - driver
    Return - driver
    Author -  Dhananjay Joshi
    Modification date - 23-Apr-2018
    """
    with driver.wait(15):
        location = driver.find_element_by_xpath("//*[@class='Location']").text
    return location