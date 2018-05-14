def compare_dictionaries(dict1, dict2, id1=None):
    """
    Function Name -  compare_dictionaries
    Description - Compares the dictionaries
    Parameters - dict1, dict2, id1=None
    Return - None
    Author -  Dhananjay Joshi
    Modification date - 24-Apr-2018
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
    Function Name -  compare_list
    Description - Compares the lists
    Parameters - act_list, exp_list
    Return - None
    Author -  Dhananjay Joshi
    Modification date - 24-Apr-2018
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
    Function Name -  verify_text
    Description - verifies text
    Parameters - act_str, exp_str
    Return - None
    Author -  Dhananjay Joshi
    Modification date - 24-Apr-2018
    """
    type_msg = 'Can not compare, {0} and {1} are different types'
    msg = "Failed to verify texts, Actual: {0}, Expected: {1}"
    assert isinstance(act_str, str) and isinstance(exp_str, str),\
        type_msg.format(type(act_str), type(exp_str))
    assert act_str.lower() == exp_str.lower(), msg.format(act_str, exp_str)


def verify(expected, actual, message=''):
    """
    Function Name -  verify
    Description -
    Parameters - expected, actual, message
    Return - None
    Author -  Dhananjay Joshi
    Modification date - 24-Apr-2018
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
    Function Name -  compare_list_of_dict
    Description -
    Parameters - act_list, exp_list, id1=None
    Return - None
    Author -  Dhananjay Joshi
    Modification date - 24-Apr-2018
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