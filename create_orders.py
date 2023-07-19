#Татьяна Долгих, 6 когорта  — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_statys_code_200():
    assert sender_stand_request.get_orders().status_code == 200