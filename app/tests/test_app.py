import time

import requests


def test_hello_flask():
    r = requests.get('http://0.0.0.0:5000')
    assert r.status_code == 200, f"expected status code 200, instead got: {r.text}"
    assert r.text == 'hello_flask', f"expected 'hello_flask' in response text, instead got: {r.text}"
