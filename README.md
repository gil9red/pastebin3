# pastebin3
A http://pastebin.com/ API wrapper for Python 3 (#python, #python3, #pastebin, #api, #wrapper)

--------------
To work needed module [Requests](https://github.com/kennethreitz/requests)

    $ pip install requests


Usage Examples
--------------

Supported version api:

```python
import pastebin3

print(pastebin3.PASTEBIN_API_VERSION)
```


**Generate a user key** (this is required by other functions):

```python
import pastebin3

api_user_key = pastebin3.api_user_key(dev_key, user_name, user_password)
print(api_user_key)
```


**paste** without api_user_key anonymous:

```python
import pastebin3

rs = pastebin3.paste(dev_key, 'Yohoho!')
print(rs)
```


User **paste** to Pastebin:

```python
import pastebin3

api_user_key = pastebin3.api_user_key(dev_key, user_name, user_password)

rs = pastebin3.paste(dev_key, 'Yohoho!', api_user_key)
print(rs)
```


Full user **paste** to Pastebin. About [format](http://pastebin.com/api#5), [private](http://pastebin.com/api#6) and [expire_date](http://pastebin.com/api#6).

```python
import pastebin3

api_user_key = pastebin3.api_user_key(dev_key, user_name, user_password)

rs = pastebin3.paste(
    dev_key,
    code='int a = 10;',
    user_key=api_user_key,
    name='foo',
    format='cpp',
    private='private',
    expire_date='10M'
)
print(rs)
```

**Delete a paste**

**paste_key** - this is the unique key of the paste you want to delete.

```python
import pastebin3

api_user_key = pastebin3.api_user_key(dev_key, user_name, user_password)

rs = pastebin3.delete_paste(dev_key, api_user_key, paste_key)
print(rs)
```


Return an XML list of all **pastes by user**.  Result limit defaults to none, so it will return all pastes:

```python
import pastebin3

api_user_key = pastebin3.api_user_key(dev_key, user_name, user_password)

# default results_limit=50
rs = pastebin3.user_pastes(dev_key, api_user_key)
print(rs)

# or:

rs = pastebin3.user_pastes(dev_key, api_user_key, results_limit=5)
print(rs)
```


Return an XML list of **User Details** of user specified by API key.

```python
import pastebin3

api_user_key = pastebin3.api_user_key(dev_key, user_name, user_password)

rs = pastebin3.user_details(dev_key, api_user_key)
print(rs)
```


Return a list of **trending pastes**. The result is in XML:

```python
import pastebin3

rs = pastebin3.trending(dev_key)
print(rs)
```


**Exceptions**:

```python
import pastebin3

try:
    api_user_key = pastebin3.api_user_key(
        dev_key=PASTEBIN_API_DEV_KEY,
        user_name=PASTEBIN_USERNAME,
        user_password=PASTEBIN_PASSWORD
    )
    print(api_user_key)
    
    rs = pastebin3.user_pastes(
        dev_key=PASTEBIN_API_DEV_KEY,
        user_key=api_user_key
    )
    print(rs)
    
    rs = pastebin3.paste(
        dev_key=PASTEBIN_API_DEV_KEY,
        code='Bugaga!',
        user_key=api_user_key,
        expire_date='10M'
    )
    print(rs)
    
except pastebin3.PastebinError as e:
    print('Error: ' + str(e))
```