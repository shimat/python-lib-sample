import requests

def google():
    r = requests.get("http://www.google.com")
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    google()
