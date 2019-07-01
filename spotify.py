import requests


def get_csrf_token():
    while True:
        csrf_request = requests.get('https://accounts.spotify.com')
        if csrf_request.status_code == 200:
            break
    return csrf_request.cookies.get("csrf_token")


def get_account_info(session, email, password):
    while True:
        response = session.get(
            'https://www.spotify.com/de/account/overview/')
        if response.status_code == 200:
            break

    admin = None

    return {"account_login": "success",
            "Username": email,
            "Password": password,
            "Admin": admin}


def spotify_check(email, password):

    api_request = requests.session()
    csrf_token = get_csrf_token()

    cookies = {
        "fb_continue": "https%3A%2F%2Fwww.spotify.com%2Fid%2F\
            account%2Foverview%2F",
        "sp_landing": "play.spotify.com%2F",
        "sp_landingref": "https%3A%2F%2Fwww.google.com%2F",
        "user_eligible": "0",
        "spot": "%7B%22t%22%3A1498061345%2C%22m%22%3A%22id\
            %22%2C%22p%22%3Anull%7D",
        "sp_t": "ac1439ee6195be76711e73dc0f79f89",
        "sp_new": "1",
        "csrf_token": csrf_token,
        "__bon": "MHwwfC0zMjQyMjQ0ODl8LTEzNjE3NDI4NTM4fDF8MXwxfDE=",
        "remember": "false@false.com",
        "_ga": "GA1.2.153026989.1498061376",
                "_gid": "GA1.2.740264023.1498061376"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS\
                X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/\
                12F69 Safari/600.1.4",
        "Accept": "application/json, text/plain",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "remember": "false",
        "username": email,
        "password": password,
        "csrf_token": csrf_token
    }

    response = api_request.post(
        "https://accounts.spotify.com/api/login",
        data=payload,
        headers=headers,
        cookies=cookies
    )

    try:
        if response.json().get("error"):
            return {
                "account_login": "error",
                "Username": email,
                "Password": password
            }
    except Exception:
        return {
            "account_login": "error",
            "Username": email,
            "Password": password
        }

    return get_account_info(api_request, email, password)


if __name__ == '__main__':
    email = 'kaqab@hi2.in'
    password = 'alpha12345'
    acc = spotify_check(email, password)
    print(acc)
