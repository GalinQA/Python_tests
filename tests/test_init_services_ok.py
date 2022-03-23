from json.decoder import JSONDecodeError
import os
import requests
import pytest
from json import loads
from pprint import pprint
from yarl import URL

# Here we get URL
HOST = URL(os.getenv("TEST_URL",'https://mfc72.dev.ocas.ai'))
MA_SESSION = os.getenv("MA_SESSION", "6ec73817-1258-408b-b412-b6e2297f168c")

data1 = {
    "limit": 100,
    "skip": 0,
    "visible": True,
    "backlist": None,
    "type": {
        "$ref": "type",
        "$id": {
            "$oid": "5b17d9df8b5670003a56b611"
        }
    }
}


def get_app_ref(url):
    response1 = requests.post(
        f"{url}/ma/search",
        json = data1,
        headers = {
            "ma_session": MA_SESSION
        }
    )
    data = loads(response1.text)
    intermediate = []
    for app in data['data']['result']:
        intermediate.append(f'app:{app["_id"]["$oid"]}')
    result = [(x,200) for x in intermediate]
    return result

def make_init(url,app_ref, code):
    response = requests.post(url/('api/init'), json={
        "v": "",
        "app_ref": app_ref,
        "services": [
            "client",
            "ma",
            "oma",
            "ws",
            "stt",
            "tts",
            "sqlr",
            "sqlr_dataset",
            "minio",
            "gjr",
            "gmc",
            "cube",
            "ds",
            "wf",
            "cf",
            "tdl",
            "toexcel",
            "cube2csv",
            "tlgrm",
            "pws"
        ]
    })
    # print(response.text)
    assert response.status_code == code
    return response.text


@pytest.mark.parametrize("app_ref, code", get_app_ref(HOST))
def test_get_check_status_code_equals_200(app_ref, code):
    make_init(HOST, app_ref, code)


