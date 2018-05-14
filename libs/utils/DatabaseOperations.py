import pymssql
import sys
from logging import error
from test_data.GlobalVariables import *

def compare_list(act_list, exp_list):
    """
    """
    if sorted(exp_list) == sorted(act_list):
        return True
    else:
        msg = 'Following item: {}, is not present in {} list'
        data = [i for i in act_list if i not in exp_list]
        data1 = [i for i in exp_list if i not in act_list]
        if data:
            raise AssertionError(msg.format(data, 'expected'))
        elif data1:
            raise AssertionError(msg.format(data1, 'actual'))


def sql(query):
    """
    """
    try:
        db_user = DATABASE_USER
        db_password = DATABASE_PASSWORD
        database = DATABASE_NAME
        db_address = DATABASE_ADDRESS
        # Connect to database and execute query.
        db_result = pymssql.connect(db_address, db_user, db_password,
                                    database).cursor()
        db_result.execute(query)
        print(db_result)
        return db_result
    except Exception as e:
        tb = sys.exc_info()[2]
        error(
            "Exception in common>>SQL. Details are - [%s]::Line Number[%s]" %
            (e.with_traceback(tb), sys.exc_info()[2].tb_lineno), True)
        raise Exception("Exception occurred in SQL ")
