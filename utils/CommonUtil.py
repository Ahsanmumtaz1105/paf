import os
import random
import string
import sys
from robot.api.logger import *
from robot.libraries.Screenshot import Screenshot

try:
    if "AutomationPOC\\" in os.getcwd():
        os.chdir("..")
        path = os.getcwd()
        sys.path.append(os.getcwd() + '\\libs')
        sys.path.append(os.getcwd() + '\\utilities')
        sys.path.append(os.getcwd() + '\\reports')
        sys.path.append(os.getcwd() + '\\setup_infra')
        sys.path.append(os.getcwd() + '\\test_runner')
        sys.path.append(os.getcwd() + '\\screens')
        sys.path.append(os.getcwd() + '\\tests')
        sys.path.append(os.getcwd() + '\\testdata')
        sys.path.append(os.getcwd() + '\\auto_it_executables')
        info("Forming and returning dynamic project path as %s " % sys.path,
             False, True)

except Exception as e1:
    tb1 = sys.exc_info()[2]
    error("Exception in CommonUtil. Details are - [%s]::Line Number[%s]" % (
        e1.with_traceback(tb1), sys.exc_info()[2].tb_lineno), True)
    raise Exception("Exception occurred in CommonUtil")


def set_project_path():
    """
    """
    try:
        while "AutomationPOC\\" in os.getcwd():
            os.chdir("..")
            # path = os.getcwd()
            sys.path.append(os.getcwd() + '\\libs')
            sys.path.append(os.getcwd() + '\\utilities')
            sys.path.append(os.getcwd() + '\\reports')
            sys.path.append(os.getcwd() + '\\setup_infra')
            sys.path.append(os.getcwd() + '\\test_runner')
            sys.path.append(os.getcwd() + '\\screens')
            sys.path.append(os.getcwd() + '\\tests')
            sys.path.append(os.getcwd() + '\\testdata')
            sys.path.append(os.getcwd() + '\\auto_it_executables')
            info("Forming and returning dynamic project path as %s " %
                 sys.path, False, True)
        if "AutomationPOC\\" in os.getcwd():
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
