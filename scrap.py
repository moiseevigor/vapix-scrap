import requests
from lxml import html

USERNAME = "igor@standard.ai"
PASSWORD = "ysjgTBI897Jj"

LOGIN_URL = "https://auth.axis.com/authn/authentication/html"
"https://auth.axis.com/authn/authentication/html?_oq=aHR0cHM6Ly93d3cuYXhpcy5jb20vbXktYXhpcy9sb2dpbj9jbGllbnRfaWQ9d3d3QXhpc0NvbV9wcm9kJnJlc3BvbnNlX3R5cGU9Y29kZSZzY29wZT1vcGVuaWQrZW1haWwrcHJvZmlsZSZyZWRpcmVjdF91cmk9aHR0cHMlM0ElMkYlMkZ3d3cuYXhpcy5jb20lMkZvcGVuaWQtY29ubmVjdCUyRmdlbmVyaWMmc3RhdGU9dTQxMFo5RHVUR1ZwYXZxV0I5N1NJV3Uydm1aRjVBWWFUOUxwbXFPRi1Bbw"

URL = "https://www.axis.com/vapix-library/license?redirect=%2F"
# URL = "https://www.axis.com/vapix-library/"
# URL = "https://www.axis.com/vapix-library/subjects/t10037719/section/t10035974/display"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    print(result.text)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "authenticity_token": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    conversation = tree.xpath("//body/div[@class='main-container']/div[@class='o2-main-container']")

    print(conversation)

    # t10035974

if __name__ == '__main__':
    main()