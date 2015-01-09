__author__ = 'ipetrash'

# # https://pypi.python.org/pypi/Pastebin/1.1.1
# # http://pythonhosted.org/Pastebin/
# # https://github.com/Morrolan/PastebinAPI
# # http://pastebin.com/u/gil9red
# # http://pastebin.com/api

import requests

class PastebinRequestError(Exception):
    pass


PASTEBIN_API_DEV_KEY = ''
PASTEBIN_USERNAME = ''
PASTEBIN_PASSWORD = ''

api_login_url = 'http://pastebin.com/api/api_login.php'
api_post_url = 'http://pastebin.com/api/api_post.php'
api_raw_url = 'http://pastebin.com/api/raw.php'

def get_api_user_key(dev_key, user_name, user_password):
    params = {
        'api_dev_key': dev_key,
        'api_user_name': user_name,
        'api_user_password': user_password,
    }

    rs = requests.post(api_login_url, data=params)

    if not rs.ok:
        raise PastebinRequestError('HTTP status code: ' + str(rs.status_code))

    if rs.text.startswith('Bad API request'):
        raise PastebinRequestError(rs.text)

    return rs.text


def get_user_pastes(dev_key, user_key, results_limit=50):
    # Pastes Created By A User
    params = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_results_limit': results_limit,
        'api_option': 'list',
    }
    rs = requests.post(api_post_url, data=params)

    if not rs.ok:
        raise PastebinRequestError('HTTP status code: ' + str(rs.status_code))

    return rs.text


def get_trending(dev_key):
    # Listing Trending Pastes
    params = {
        'api_dev_key': dev_key,
        'api_option': 'trends',
    }
    rs = requests.post(api_post_url, data=params)

    if not rs.ok:
        raise PastebinRequestError('HTTP status code: ' + str(rs.status_code))

    if rs.text.startswith('Bad API request'):
        raise PastebinRequestError(rs.text)

    return rs.text


def paste(dev_key, code, user_key=None, name=None, format=None, private=None, expire_date=None):
    # TODO: support when private=2
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
    rs = requests.post(api_post_url, data=params)

    if not rs.ok:
        raise PastebinRequestError('HTTP status code: ' + str(rs.status_code))

    if rs.text.startswith('Bad API request'):
        raise PastebinRequestError(rs.text)

    return rs.text


def delete_paste(dev_key, user_key, paste_key):
    params = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_paste_key': paste_key,
        'api_option': 'delete',
    }
    rs = requests.post(api_post_url, data=params)

    if not rs.ok:
        raise PastebinRequestError('HTTP status code: ' + str(rs.status_code))

    if rs.text.startswith('Paste Removed'):
        return True

    elif rs.text.startswith('Bad API request'):
        raise PastebinRequestError(rs.text)

    return False


def get_user_details(dev_key, user_key):
    params = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_option': 'userdetails',
    }
    rs = requests.post(api_post_url, data=params)

    if not rs.ok:
        raise PastebinRequestError('HTTP status code: ' + str(rs.status_code))

    if rs.text.startswith('Bad API request'):
        raise PastebinRequestError(rs.text)

    return rs.text


if __name__ == '__main__':
    try:
        api_user_key = get_api_user_key(PASTEBIN_API_DEV_KEY, PASTEBIN_USERNAME, PASTEBIN_PASSWORD)
        print(api_user_key)

        # rs = get_user_pastes(PASTEBIN_API_DEV_KEY, api_user_key)
        # print(rs)
        #
        # rs = get_trending(PASTEBIN_API_DEV_KEY)
        # print(rs)

        rs = paste(dev_key=PASTEBIN_API_DEV_KEY,
                   code='bugaga!',
                   user_key=api_user_key,
                   name='Foo',
                   format='c',
                   private=2,
                   expire_date='10M'
                   )
        print(rs)

        # rs = delete_paste(
        #     dev_key=PASTEBIN_API_DEV_KEY,
        #     user_key=api_user_key,
        #     paste_key='wURpabdc'
        # )
        # print(rs)

        # rs = get_user_details(
        #     dev_key=PASTEBIN_API_DEV_KEY,
        #     user_key=api_user_key
        # )
        # print(rs)


    except PastebinRequestError as e:
        print('Error: ' + str(e))