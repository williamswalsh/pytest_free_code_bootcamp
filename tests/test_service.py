import pytest
import requests

import source.service as service
import unittest.mock as mock


# Point to the file where the function you want to mock is:
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    # Set the return value
    mock_get_user_from_db.return_value = "Mocked Alice"

    # do the call to the mocked method
    user_name = service.get_user_from_db(1)

    # Assert the return value
    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_requests_get.return_value = mock_response

    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_http_error(mock_requests_get):
    mock_response = mock.Mock()

    # Unauthorised HTTP Status Code
    mock_response.status_code = 401

    # set return value
    mock_requests_get.return_value = mock_response

    # capture the exception created from the get_users() method
    with pytest.raises(requests.HTTPError):
        service.get_users()
