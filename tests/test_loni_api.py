import pytest
import loni_api.loniapi as loniapi

loniAPI = loniapi.LoniAPI()

def test_login1():
    loniAPI = loniapi.LoniAPI()
    assert loniAPI.login("ampad") == 1

def test__login2():
    loniAPI = loniapi.LoniAPI()
    loniAPI.login("ampad")
    assert loniAPI.group_id == "ampad"


def test__logout1():
    loniAPI = loniapi.LoniAPI()
    loniAPI.login("ampad")
    loniAPI.logout()
    assert loniAPI._auth_key is None
