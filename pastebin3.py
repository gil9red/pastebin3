#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from urllib.request import urlopen, Request
from urllib.parse import urlencode


# SOURCE: https://pastebin.com/doc_api


class PastebinError(Exception):
    pass


class PastebinRequestError(PastebinError):
    pass


# TODO: docstring
# TODO: correct comments and strings: my bad english :(


PASTEBIN_API_VERSION = '3.1'

__API_LOGIN_URL = 'https://pastebin.com/api/api_login.php'
__API_POST_URL = 'https://pastebin.com/api/api_post.php'

# We have 3 valid values available which you can use with the 'api_paste_private' parameter:
__PRIVATE_VARIANTS = {
    'public': 0,
    'unlisted': 1,
    'private': 2
}


def __send_post_request_by_pastebin(url: str, params: dict) -> str:
    """

    :param url:
    :param params:
    :return:
    """

    # Remove None params
    params = {
        k: v
        for k, v in params.items()
        if v
    }
    params = urlencode(params).encode('utf-8')

    # POST request
    req = Request(url, data=params)

    with urlopen(req) as f:
        if f.getcode() != 200:
            raise PastebinRequestError('HTTP status code: ' + str(f.getcode()))

        rs = f.read().decode("utf-8")

        if rs.startswith('Bad API request'):
            raise PastebinRequestError(rs)

        return rs


def __send_api_post_request(params: dict) -> str:
    return __send_post_request_by_pastebin(__API_POST_URL, params)


def api_user_key(dev_key: str, user_name: str, user_password: str) -> str:
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
    return __send_post_request_by_pastebin(__API_LOGIN_URL, params)


def user_pastes(dev_key: str, user_key: str, results_limit=50) -> str:
    """ Listing Pastes Created By A User

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

    rs = __send_api_post_request(params)
    return rs


def trending(dev_key) -> str:
    """ Listing Trending Pastes

    :param dev_key:
    :return:
    """

    params = {
        'api_dev_key': dev_key,
        'api_option': 'trends',
    }
    return __send_api_post_request(params)


def paste(
        dev_key: str,
        code: str,
        user_key: str = None,
        name: str = None,
        format: str = None,
        private: str = None,
        expire_date: str = None
) -> str:
    """ Creating A New Paste

    :param dev_key:
    :param code:
    :param user_key:
    :param name:
    :param format:
    :param private:
    :param expire_date:
    :return:
    """

    if private:
        private = __PRIVATE_VARIANTS.get(private.lower())

        if private == 2 and not user_key:
            raise PastebinError('Private paste only allowed in combination with api_user_key, '
                                'as you have to be logged into your account to access the paste')

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
    return __send_api_post_request(params)


def delete_paste(dev_key: str, user_key: str, paste_key: str) -> bool:
    """ Deleting A Paste Created By A User

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

    rs = __send_api_post_request(params)
    return rs.startswith('Paste Removed')


def user_details(dev_key: str, user_key: str) -> str:
    """ Getting A Users Information And Settings

    :param dev_key:
    :param user_key:
    :return:
    """

    params = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_option': 'userdetails',
    }
    return __send_api_post_request(params)


if __name__ == '__main__':
    dev_key = ...
    user_name = ...
    user_password = ...
    api_user_key = api_user_key(dev_key, user_name, user_password)
    print(api_user_key)

    rs = paste(dev_key, 'Yohoho!', api_user_key)
    print(rs)

    rs = paste(
        dev_key,
        code='int a = 10;',
        user_key=api_user_key,
        name='foo',
        format='cpp',
        private='private',
        expire_date='10M'
    )
    print(rs)
