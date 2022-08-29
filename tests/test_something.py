import requests
from PytestRep.configuration import SERVICE_URL
from PytestRep.src.enums.global_enums import GlobalErrorMessages


def test_get_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
