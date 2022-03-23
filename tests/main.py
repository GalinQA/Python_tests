# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import requests


def test_get_check_status_code_equals_200():
    response = requests.get("https://yandex.ru/")
    assert response.status_code == 200


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
