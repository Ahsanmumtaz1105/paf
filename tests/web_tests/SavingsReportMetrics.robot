*** Settings ***
Documentation    Regression test case to test savings report metrics changed on UI are getting reflected in Database

Library           ../../libs/utils/CommonUtil.py
Library           ../../libs/Drivers.py
Library           ../../screens/web_system_manager/LoginPage.py
Library           ../../screens/web_system_manager/accounts/Users.py
Library           ../../screens/web_system_manager/system_config/global_config/SavingsReportMetrics.py
Library           ../../libs/utils/DatabaseOperations.py
Variables         ../../test_data/GlobalVariables.py

Suite Setup       set project path

*** Variables ***
${MEASUREMENT_SYSTEM}  Metric
${ONE_TREE_EQUIVALENT_VALUE}  10671
${ONE_PAGE_USES_VALUE}  0.5531
${ONE_KG_PAGE_RELEASES_VALUE}  8.80


*** Test Cases ***
Save Report Metrics
    [Tags]    REGRESSION

    # Get selenium web driver instance
    ${DRIVER}  get_selenium_web_driver_instance  ${BROWSER}

    # Login to equitrac application
    login_to_equitrac_web_system_manager_as_admin  ${DRIVER}  ${USER_NAME}  ${PASSWORD}  ${MACHINE_NAME}

    # Navigate to "Savings report metrics" page and verify navigation is successful
    navigate to savings report metrics page  ${DRIVER}

    # Change the mesasurement system to metric
    select measurement system  ${DRIVER}  ${MEASUREMENT_SYSTEM}

    # Set one tree is equivalent to value
    set one tree is equivalent to value  ${DRIVER}  ${ONE_TREE_EQUIVALENT_VALUE}

    # Set one page uses to value
    set one page uses to value  ${DRIVER}  ${ONE_PAGE_USES_VALUE}

    # Set one KG of paper releases to value
    set one kg of paper release to value  ${DRIVER}  ${ONE_KG_PAGE_RELEASES_VALUE}

    # Save and verify the changes in report saving report metrics
    save changes to report metrics  ${DRIVER}

    # Verify values are updated in database
    verify savings report metrics values in database  ${MEASUREMENT_SYSTEM}  ${ONE_TREE_EQUIVALENT_VALUE}  ${ONE_PAGE_USES_VALUE}  ${ONE_KG_PAGE_RELEASES_VALUE}

    # Logout from application
    log out  ${Driver}

    # Tear down code
    [Teardown]      close_driver