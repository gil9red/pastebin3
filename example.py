__author__ = 'ipetrash'


PASTEBIN_API_DEV_KEY = ''
PASTEBIN_USERNAME = ''
PASTEBIN_PASSWORD = ''


from pastebin3 import *


if __name__ == '__main__':
    try:
        api_user_key = get_api_user_key(PASTEBIN_API_DEV_KEY, PASTEBIN_USERNAME, PASTEBIN_PASSWORD)
        print(api_user_key)
        #
        # rs = get_user_pastes(PASTEBIN_API_DEV_KEY, api_user_key)
        # print(rs)
        #
        # rs = get_trending(PASTEBIN_API_DEV_KEY)
        # print(rs)

        # rs = paste(dev_key=PASTEBIN_API_DEV_KEY,
        #            code='bugaga!',
        #            user_key=api_user_key,
        #            name='Foo',
        #            format='c',
        #            private=2,
        #            expire_date='10M'
        #            )
        # print(rs)

        # rs = delete_paste(
        #     dev_key=PASTEBIN_API_DEV_KEY,
        #     user_key=api_user_key,
        #     paste_key='Ryivcxkg'
        # )
        # print(rs)

        # rs = get_user_details(
        #     dev_key=PASTEBIN_API_DEV_KEY,
        #     user_key=api_user_key
        # )
        # print(rs)


    except PastebinRequestError as e:
        print('Error: ' + str(e))