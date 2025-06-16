from main import get_weather,add,divide
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