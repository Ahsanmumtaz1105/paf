import os
import sys
from robot.api.logger import *


def run_auto_it_executables(path_to_executable, argument):
    """
    Function Name -  run_auto_it_executables
    Description - This method runs auto it executables
    Parameters - path_to_executable, argument
    Return - Web driver
    Author -  Dhananjay Joshi
    Modification date - 03-May-2018
    """
    try:
        path_to_executable = \
            os.getcwd() + "\\libs\\auto_it_executables\\" + path_to_executable\
            + " " \
            + argument
        os.system(path_to_executable)
        info("Running '%s' AutoIt executable with arguments '%s'" %
             (path_to_executable, argument), False, True)
    except Exception as e:
        tb = sys.exc_info()[2]
        error(
            "Exception in run_auto_it_executables. Details are - [%s]::Line "
            "Number[%s]" % (e.with_traceback(tb), sys.exc_info()[2].tb_lineno),
            True)
        raise Exception("Exception occurred in SQL ")