import requests

produto = "https://br.puma.com/pd/bone-puma-x-kidsuper-baseball/026601.html"
params = {
    'color': '01',
}

def monitor():
    response = requests.get(produto, params=params)
    print(response.status_code)
    print(response.text)

monitor()