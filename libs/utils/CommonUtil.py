import os
import random
import string
import sys
from robot.api.logger import *
from robot.libraries.Screenshot import Screenshot

try:
    while "paf\\" in os.getcwd():
        os.chdir("..")
        # path = os.getcwd()
    sys.path.append(os.getcwd() + '\\libs')
    sys.path.append(os.getcwd() + '\\libs\\utils')
    sys.path.append(os.getcwd() + '\\reports')
    sys.path.append(os.getcwd() + '\\setup_infra')
    sys.path.append(os.getcwd() + '\\test_runner')
    sys.path.append(os.getcwd() + '\\screens')
    sys.path.append(os.getcwd() + '\\tests')
    sys.path.append(os.getcwd() + '\\test_data')
    sys.path.append(os.getcwd() + '\\libs\\auto_it_executables')
    info("Forming and returning dynamic project path as %s " %
         sys.path,False,True)

except Exception as e1:
    tb1 = sys.exc_info()[2]
    error("Exception in CommonUtil. Details are - [%s]::Line Number[%s]" % (
        e1.with_traceback(tb1), sys.exc_info()[2].tb_lineno), True)
    raise Exception("Exception occurred in CommonUtil")


def set_project_path():
    """
    """
    try:
        while "paf\\" in os.getcwd():
            os.chdir("..")
            # path = os.getcwd()
        sys.path.append(os.getcwd() + '\\libs')
        sys.path.append(os.getcwd() + '\\libs\\utils')
        sys.path.append(os.getcwd() + '\\reports')
        sys.path.append(os.getcwd() + '\\setup_infra')
        sys.path.append(os.getcwd() + '\\test_runner')
        sys.path.append(os.getcwd() + '\\screens')
        sys.path.append(os.getcwd() + '\\tests')
        sys.path.append(os.getcwd() + '\\test_data')
        sys.path.append(os.getcwd() + '\\libs\\auto_it_executables')
        info("Forming and returning dynamic project path as %s " %
             sys.path,False,True)
        if "paf\\" in os.getcwd():
            os.chdir("..")
        path = os.getcwd()
        return path
    except Exception as e:
        tb = sys.exc_info()[2]
        error("Exception in set_project_path. Details are - [%s]::"
              "Line Number[%s]" % (e.with_traceback(tb),
                                   sys.exc_info()[2].tb_lineno), True)
        raise Exception("Exception occurred in set_project_path")


def get_project_path():
    """
    """
    try:
        return os.getcwd()
    except Exception as e:
        tb = sys.exc_info()[2]
        error("Exception in get_project_path. Details are - [%s]::"
              "Line Number[%s]" % (e.with_traceback(tb),
                                   sys.exc_info()[2].tb_lineno), True)
        raise Exception("Exception occurred in get_project_path")


def take_desktop_screenshot(file_name):
    """
    """
    try:
        file_name = Screenshot().take_screenshot(file_name)
        info("Screenshot taken with screenshot name as [%s]" % file_name,
             True, True)
    except Exception as e:
        tb = sys.exc_info()[2]
        error("Exception in take_desktop_screenshot. Details are - [%s]::"
              "Line Number[%s]" % (e.with_traceback(tb),
                                   sys.exc_info()[2].tb_lineno), True)
        raise Exception("Exception occurred in take_desktop_screenshot")


def random_string_generator(
        size=2, chars=string.ascii_lowercase + string.digits):
    """
    """
    try:
        return ''.join(random.choice(chars) for _ in range(int(size)))
    except Exception as e:
        tb = sys.exc_info()[2]
        error("Exception in random_string_generator. Details are - [%s]::"
              "Line Number[%s]" % (e.with_traceback(tb),
                                   sys.exc_info()[2].tb_lineno), True)
        raise Exception("Exception occurred in random_string_generator")


def get_print_file_path(file_name):
    """
    """
    try:
        return str(get_project_path()) + file_name
    except Exception as e:
        error("Exception thrown in get_print_file_path as  [%s]" % repr(e),
              True)


def compare_dictionaries(dict1, dict2, id1=None):
    """
    """
    if dict1 is None and dict2 is None:
        return True, "Both the dictionaries are None"

    if dict1 is None or dict2 is None:
        return False, "One of the dictionary contains None"

    if (type(dict1) is not dict) or (type(dict2) is not dict):
        return False, "One of the dictionary is not a dict type, dict1 %s" \
                      " dict2 %s " % (type(dict1), type(dict2))

    shared_keys = set(dict1.keys()) & set(dict2.keys())
    if len(shared_keys) != len(dict1.keys()) or len(shared_keys) != len(
            dict2.keys()):
        return False, "Dictionary Keys mismatched dict1 %s ," \
                      "dict2 %s , sharedKeys %s " \
               % (dict1.keys(), dict2.keys(), shared_keys)
    dicts_are_equal = True
    for key in dict1.keys():
        if type(dict1[key]) is dict:
            result, message = compare_dictionaries(dict1[key], dict2[key])
            if result is False:
                return result, message
        elif type(dict1[key]) is list:
            # If list contains dict
            if id1:
                result2, message2 = compare_list_of_dict(
                    dict1[key], dict2[key], id1=id1)
                if result2 is False:
                    return result2, message2
        else:
            if dict1[key] != dict2[key]:
                dicts_are_equal = False
                return False, "Dictionaries value mismatched, dict1  %s:%s," \
                              " dict2 %s:%s" % (key, dict1[key], key,
                                                dict2[key])
    return dicts_are_equal, "Dictionaries are equal"


def compare_list(act_list, exp_list):
    """
    """
    if sorted(exp_list) == sorted(act_list):
        return
    else:
        msg = 'Following item: {}, is not present in {} list'
        data = [i for i in act_list if i not in exp_list]
        data1 = [i for i in exp_list if i not in act_list]
        if data:
            raise AssertionError(msg.format(data, 'expected'))
        elif data1:
            raise AssertionError(msg.format(data1, 'actual'))


def verify_text(act_str, exp_str):
    """
    """
    type_msg = 'Can not compare, {0} and {1} are different types'
    msg = "Failed to verify texts, Actual: {0}, Expected: {1}"
    assert isinstance(act_str, str) and isinstance(exp_str, str),\
        type_msg.format(type(act_str), type(exp_str))
    assert act_str.lower() == exp_str.lower(), msg.format(act_str, exp_str)


def verify(expected, actual, message=''):
    """
    """
    check_type = type(expected)
    if type(expected) != type(actual):
        print("Type mismatched. Expected type {0} . Actual Type "
              "{1}".format(type(expected), type(actual)))
        return False

    elif check_type is not str and check_type is not int and check_type is \
            not float and check_type is not list and check_type is not dict:
        print('Compares only str, float, int, list of dict type objects')
        return False
    # -------------------------------------------------------------------------
    # Compare dictionaries.
    elif type(expected) is dict:
        input_text_matches, message = compare_dictionaries(expected, actual)
        if input_text_matches is False:
            print(message)
            return False
        else:
            return True
    # -------------------------------------------------------------------------
    #  Compare List
    elif type(expected) is list:
        # pdb.set_trace()
        if len(expected) != len(actual):
            print(
                message +
                " Validation Failed. List Length mismatch. Expected len {0}  "
                "Actual Len {1}. ".format(len(expected), len(actual)))
        common_item = []
        for item in expected:
            if item in actual:
                common_item.append(item)
                continue

    elif check_type is int or check_type is float or check_type is str:
        if expected != actual:
            print(message + " Validation Failed, Expected Value: {0}, Actual "
                            "Value: {1} .".format(expected, actual))
            return False
        else:
            return True


def compare_list_of_dict(act_list, exp_list, id1=None):
    """
    """
    if len(act_list) != len(exp_list):
        return False, "list length mismatched"
    for item in exp_list:
        if isinstance(item, dict):
            for item2 in act_list:
                if item[id1] == item2[id1]:
                    result, message = compare_dictionaries(item, item2)
                    if result is False:
                        return result, message
                    else:
                        break
                else:
                    continue
            else:
                return False, "Dictionaries value mismatched,  dict1: %s and "\
                               % (item[id1])
        else:
            return False, 'Not a dictionary'
    return True, "Dictionaries are equal"
