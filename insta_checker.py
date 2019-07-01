import requests
import requests
import json


base_url = 'https://www.instagram.com/'
login_url = base_url + 'accounts/login/'
#login_url = 'https://www.instagram.com/accounts/login/'
username = 'kaqab@hi2.in'
password = 'alpha12345'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'

session = requests.session()
session.headers = {'user-agent': user_agent}
session.headers.update({'Referer': base_url})

req = session.get(base_url)
session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
login_data = {
    'username': username,
    'password': password
}
login = session.post(login_url, data=login_data, allow_redirects=True)
session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
cookies = login.cookies
print(login.content)
#login_text = json.loads(login.text)
#print(login_text)