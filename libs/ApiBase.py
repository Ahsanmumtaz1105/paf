import json
import re
import socket
import sys
import requests
import urllib3
from robot.api.logger import *

urllib3.disable_warnings()


class ApiBase:
    """
    """
    session = None
    response = None
    result = None
    token = None
    data = None
    api_url = None
    message = None
    headers = None
    flag = True

    @staticmethod
    def api_login(user_name, password, host_url=None):
        """
        """
        try:
            if host_url is None:
                host_url = r"https://{}/EQWebClient".format(
                    socket.gethostname())
            else:
                host_url = r"https://{}/EQWebClient".format(host_url)

            info("Url formed in api_login is %s:: " % host_url, True, True)

            ApiBase.session = requests.session()
            ApiBase.session.verify = False
            ApiBase.response = ApiBase.session.get(host_url)
            ApiBase.result = re.search(
                r'<input.*name="__RequestVerificationToken".*value="(.*?)"',
                ApiBase.response.text)
            ApiBase.token = ApiBase.result.group(1)
            ApiBase.data = {"__RequestVerificationToken": ApiBase.token,
                            "UserName": user_name, "Password": password}

            ApiBase.result = ApiBase.session.post(host_url + "/Login/Login",
                                                  data=ApiBase.data)
            if ApiBase.result.status_code == requests.codes.ok:
                print("Successfully Log in.")

                ApiBase.api_url = host_url + "/systemmanager/api/"
                ApiBase.message = \
                    "Wrong http status code. Expected {0}, Actual {1}"
                ApiBase.headers = \
                    {'Accept': 'application/json', 'Content-Type':
                        'application/json'}

            return ApiBase.session, ApiBase.api_url
        except Exception as e:
            tb = sys.exc_info()[2]
            error("Exception in def api_login as  [%s]::"
                  "Line Number[%s]" % (e.with_traceback(tb),
                                       sys.exc_info()[2].tb_lineno), True)
            raise Exception("Exception occurred in api_login ")

    @staticmethod
    def get_and_verify(url):
        """
        """
        try:
            ApiBase.result = ApiBase.session.get(url, headers=ApiBase.headers)
            return ApiBase.result
        except Exception as e:
            tb = sys.exc_info()[2]
            error("Exception in api_base>>get_and_verify. Details are - "
                  "[%s]::Line Number[%s]" % (e.with_traceback(tb),
                                             sys.exc_info()[2].tb_lineno),
                  True)
            raise Exception("Unable to send get request")

    @staticmethod
    def post_and_verify(url, data):
        """
        """
        info("data: %s" % data, True, True)
        try:
            # data = json.loads(data)
            info("Inside put_and_verify:: with parameters %s::%s " % (
                url, data), True, True)
            res = ApiBase.session.post(
                url, json=data, headers=ApiBase.headers, verify=False)
            return res.status_code
        except Exception as e:
            tb = sys.exc_info()[2]
            error(
                "Exception in api_base>>put_and_verify. Details are - [%s]::"
                "Line Number[%s]" % (e.with_traceback(tb),
                                     sys.exc_info()[2].tb_lineno), True)
            raise Exception("Unable to send put request")

    @staticmethod
    def put_and_verify(url, test_data, entity_id=None):
        """
        """
        try:
            if entity_id:
                url += "/" + str(entity_id)
            info("url data: %s" % url, True, True)

            try:
                test_data = json.loads(test_data)
            except:
                test_data = json.dumps(test_data)
            info("Inside put_and_verify:: with parameters %s::%s "
                 % (url, test_data), True, True)
            ApiBase.result = ApiBase.session.put(url, json=test_data,
                                                 headers=ApiBase.headers,
                                                 verify=False)
            return ApiBase.result.status_code
        except Exception as e:
            tb = sys.exc_info()[2]
            error("Exception in api_base>>put_and_verify. Details are - "
                  "[%s]::Line Number[%s]" % (e.with_traceback(tb),
                                             sys.exc_info()[2].tb_lineno),
                  True)
            raise Exception("Unable to send put request")


    @staticmethod
    def delete_and_verify(url, id1):
        """
        """
        try:
            res = ApiBase.session.delete(
                url + '/{}'.format(id1), headers=ApiBase.headers)
            return res
        except Exception as e:
            tb = sys.exc_info()[2]
            error(
                "Exception in api_base>>delete_and_verify. Details are - [%s]::"
                "Line Number[%s]" % (e.with_traceback(tb),
                                     sys.exc_info()[2].tb_lineno), True)
            raise Exception("Unable to send get request")

    @staticmethod
    def verify_status_code(response, exp_code=500):
        """
        """
        code = response.status_code
        assert code == exp_code, ApiBase.message.format(exp_code, code)

    @staticmethod
    def verify_two_dictionary(resp1, test_data_default):
        """
        """
        try:
            if resp1 == test_data_default:
                ApiBase.flag = True
                print("pass")
            elif resp1 is None or test_data_default is None:
                ApiBase.flag = False
                raise Exception(
                    "Data is None. Data mis match. Expected {}, "
                    "Actual {}".format(test_data_default, resp1))
            else:
                ApiBase.flag = False
                raise Exception("Data mis match. Expected {}, Actual {}".
                                format(test_data_default, resp1))
        except Exception as e:
            tb = sys.exc_info()[2]
            error("Exception in api_base >>verify_two_dictionary. Details are "
                  "- [%s]::Line Number[%s]" % (e.with_traceback(tb),
                                               sys.exc_info()[2].tb_lineno),
                  True)
            ApiBase.flag = False
            return ApiBase.flag
