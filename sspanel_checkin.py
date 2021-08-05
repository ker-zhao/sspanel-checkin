import os
import requests


def push_message(send_key, title, body):
    url = 'https://sc.ftqq.com/{}.send'.format(send_key)
    data = {
        'text': title,
        'desp': body,
    }
    requests.post(url=url, data=data)


def main():
    user_info = os.environ['USER_INFO']
    send_key = os.environ['SEND_KEY'] if "SEND_KEY" in os.environ else ""
    base_url, email, password = user_info.split("|")
    login_url = base_url + '/auth/login'
    checkin_url = base_url + '/user/checkin'

    with requests.sessions.Session() as session:
        post_data = {"email": email, "passwd": password, "code": ""}
        session.post(login_url, post_data)
        res = session.post(checkin_url)
    # message = str(res.json())
    message = res.content.decode('unicode_escape')
    print(message)
    if send_key:
        push_message(send_key, "SSPanel报名结果", message)


if __name__ == "__main__":
    main()
