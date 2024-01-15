import requests

def getData(url):
    data = requests.get(url).json()

    return data