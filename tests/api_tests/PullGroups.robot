*** Settings ***
Documentation    Unit test case

Library  ../../libs/utils/CommonUtil.py
Library  ../../libs/ApiBase.py
Library  Collections
Variables  ../../test_data/GlobalVariables.py
Library  Builtin
Library  Collections

Suite Setup       set project path

*** Test Cases ***
Pull Groups
    [Tags]    UNITTEST
    ${output}    api login  ${username}  ${password}  ${machine_name}
    ${full_url}     set variable  @{output}[1]pullgroups

    ${data}     create dictionary  Name=test_pg1
    ${res1}     post and verify  ${full_url}    ${data}

    ${resp}     get and verify  ${full_url}
    ${id}       set variable  @{resp.json()}

    ${update_data}      create dictionary  Name=test_pg1_update
    ${res2}     put and verify  ${full_url}     ${update_data}      ${id['Id']}

    ${del_res}      delete and verify  ${full_url}  ${id['Id']}

#    ${response}  get and verify


