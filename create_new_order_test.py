# Игнатова Анастасия, 12-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data


def post_new_order(body):    # cоздание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_USER_ORDERS, # подставляем полный url
                         json=body) # тут тело

order_track = post_new_order(data.order_body).json()["track"]  # Сохранение номер отслеживания заказа
#response = post_new_order(data.order_body);
#print(response.status_code)
#print(response.json())


def get_order(order_track):     # получение заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_TRACK_ORDERS + str(order_track))

def test_get_order():
    response = post_new_order(data.order_body)
    track = response.json()["track"]
    #print("Номер заказа:",track)


    data_order = get_order(order_track)
    assert data_order.status_code == 200