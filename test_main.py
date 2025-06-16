from main import get_weather,add,divide, UserManager
import pytest

def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(21) == "hot"

def test_add():
    assert add(2,3)==5, "2+3 shouold be 5"
    assert add(-1,3)==2, "-1+2 shouold be 2"
    assert add(0,0)==0, "0+0 shouold be 0"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by 0"):
        divide(10,0)




@pytest.fixture #Fresh instance before each test
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe","john@example.com") ==True
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_duplicate_user(user_manager):
    user_manager.add_user("john_doe","john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe","john@example.com")



def test_get_weather(mocker):
    mock_get = mocker.patch("main.requests.get")

    #Setting return values
    mock_get.return_value.status_code =200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition" : "Sunny"}

    result=get_weather("Dubai")

    assert result == {"temperature" : 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("http://api.weather.com/v1/Dubai")