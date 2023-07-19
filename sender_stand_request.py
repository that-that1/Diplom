import requests
import URL
import data

def post_new_orders(body):
    response = requests.post(URL.URL_s + URL.POST_orders,
                             json=body)
    return response.json()['track']

def get_orders():
    track = str(post_new_orders(data.body))
    response = requests.get(URL.URL_s + URL.GET_orders + track)
    return response