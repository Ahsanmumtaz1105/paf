*** Settings ***
Library           ../../libs/utils/CommonUtil.py
Library           ../../libs/auto_it_executables/RunAutoitScripts.py
Library           ../../libs/utils/ExcelOperations.py
Library           ../../libs/ApiBase.py
Library           ../../libs/Drivers.py
Library           ../../screens/web_system_manager/LoginPage.py
Library           ../../screens/web_system_manager/system_config/LandingUserPage.py
Library           ../../screens/web_system_manager/accounts/Users.py
Library           ../../setup_infra/SetupVM.py
Variables         ../../test_data/GlobalVariables.py

Suite Setup       set project path

*** Test Cases ***
Auto Pin Management
    [Documentation]     Verifying Automated Pin Code Management.
    ...                 Setting up the API.
    ...                 Enable Automated Pincode Management through API.
    ...                 Add user and verify Pins are generated.
    ...                 Verify User is able to login with generated pins


    ${request_input}    get cell data from excel  APIs Test Data.xlsx   AutomatedPinCodeManagement  2   5
    ${api_url}    get cell data from excel  APIs Test Data.xlsx   AutomatedPinCodeManagement  2   2
    ${output}    api login  ${USER_NAME}     ${PASSWORD}     ${MACHINE_NAME}

    ${request_input}    get cell data from excel  APIs Test Data.xlsx   AutomatedPinCodeManagement  3   5
    ${api_url}    get cell data from excel  APIs Test Data.xlsx   AutomatedPinCodeManagement  3   2
    ${responseoutput}   put and verify  @{output}[1]${api_url}    ${request_input}
    should be equal as strings      ${responseoutput}   200

    ${request_input}    get cell data from excel  APIs Test Data.xlsx   AutomatedPinCodeManagement  2   5
    ${api_url}    get cell data from excel  APIs Test Data.xlsx   AutomatedPinCodeManagement  2   2
    ${responseoutput}   put and verify  @{output}[1]${api_url}    ${request_input}
    should be equal as strings      ${responseoutput}   200


    ${Driver}   get_selenium_web_driver_instance  chrome
    login_to_equitrac_web_system_manager_as_admin     ${Driver}    ${USER_NAME}     ${PASSWORD}     ${MACHINE_NAME}
    open users page     ${Driver}
    ${username}     random string generator
    ${printfiledocname}     random string generator  5
    create users details    ${Driver}   ${USER_NAME}  ${USER_NAME}  ${USER_EMAIL}
    ${info}     get users detail    ${Driver}   ${USER_NAME}
    log out     ${Driver}
    login to equitrac web system manager as non admin       ${Driver}   ${info['primaryPIN']}     ${info['sencondaryPIN']}     ${MACHINE_NAME}

    ${printfile_path}     get print_file path    \\test_data\\sample.txt
    run_auto_it_executables      PrintFromNotepad.exe   ${printfile_path} "I-Queue"
    run_auto_it_executables  LoginToEqPrintClient.exe  ${info['primaryPIN']} ${info['sencondaryPIN']} ${printfiledocname}

    [Teardown]      close_driver