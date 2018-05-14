import pymssql
import xmltodict
import sys
from logging import error


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


def compare_list(act_list, exp_list):
    """
    Function Name -  compare_list
    Description - Compares 2 lists
    Parameters - list 1, list 2
    Return - None
    Author -  Amol Chitte
    Modification date - 24-Apr-2018
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
    Function Name -  SQL
    Description - Queries the database table
    Parameters - query
    Return - None
    Author -  Amol Chitte
    Modification date - 24-Apr-2018
    """
    try:
        db_user = r'ivt-regression.com\pune_ivt'
        db_password = 'Equitrac1'
        database = 'eqcas'
        db_address = '10.66.28.119:1433'
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