__author__ = 'ipetrash'

# # https://pypi.python.org/pypi/Pastebin/1.1.1
# # http://pythonhosted.org/Pastebin/
# # https://github.com/Morrolan/PastebinAPI
# # http://pastebin.com/u/gil9red
# # http://pastebin.com/api

import requests


class PastebinRequestError(Exception):
    pass


# TODO: requests replaced by urllib
# TODO: docstring


PASTEBIN_API_VERSION = '3.1'

API_LOGIN_URL = 'http://pastebin.com/api/api_login.php'
API_POST_URL = 'http://pastebin.com/api/api_post.php'


def send_post_request_by_pastebin(url, params):
    """

    :param url:
    :param params:
    :return:
    """

    rs = requests.post(url, data=params)

    if not rs.ok:
        raise PastebinRequestError('HTTP status code: ' + str(rs.status_code))

    if rs.text.startswith('Bad API request'):
        raise PastebinRequestError(rs.text)

    return rs


def get_api_user_key(dev_key, user_name, user_password):
    """

    :param dev_key:
    :param user_name:
    :param user_password:
    :return:
    """

    params = {
        'api_dev_key': dev_key,
        'api_user_name': user_name,
        'api_user_password': user_password,
    }

    rs = send_post_request_by_pastebin(API_LOGIN_URL, params)
    return rs.text


def get_user_pastes(dev_key, user_key, results_limit=50):
    """ Pastes Created By A User

    :param dev_key:
    :param user_key:
    :param results_limit:
    :return:
    """

    params = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_results_limit': results_limit,
        'api_option': 'list',
    }

    rs = send_post_request_by_pastebin(API_POST_URL, params)
    return rs.text


def get_trending(dev_key):
    """ Listing Trending Pastes

    :param dev_key:
    :return:
    """

    params = {
        'api_dev_key': dev_key,
        'api_option': 'trends',
    }

    rs = send_post_request_by_pastebin(API_POST_URL, params)
    return rs.text


def paste(dev_key, code, user_key=None, name=None, format=None, private=None, expire_date=None):
    """

    :param dev_key:
    :param code:
    :param user_key:
    :param name:
    :param format:
    :param private:
    :param expire_date:
    :return:
    """


    # TODO: support when private=2
    # TODO: support string private
    # private:
    # 0 = Public
    # 1 = Unlisted
    # 2 = Private (only allowed in combination with api_user_key, as you have to be logged
    # into your account to access the paste)

    params = {
        'api_dev_key': dev_key,
        'api_option': 'paste',
        'api_paste_code': code,

        'api_user_key': user_key,
        'api_paste_name': name,
        'api_paste_format': format,
        'api_paste_private': private,
        'api_paste_expire_date': expire_date,
    }

    rs = send_post_request_by_pastebin(API_POST_URL, params)
    return rs.text


def delete_paste(dev_key, user_key, paste_key):
    """

    :param dev_key:
    :param user_key:
    :param paste_key:
    :return:
    """

    params = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_paste_key': paste_key,
        'api_option': 'delete',
    }

    rs = send_post_request_by_pastebin(API_POST_URL, params)
    if rs.text.startswith('Paste Removed'):
        return True

    return False


def get_user_details(dev_key, user_key):
    """

    :param dev_key:
    :param user_key:
    :return:
    """

    params = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_option': 'userdetails',
    }

    rs = send_post_request_by_pastebin(API_POST_URL, params)
    return rs.text