import pytest
from working import convert

def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"

def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("17:00 AM to 5 PM") 
    with pytest.raises(ValueError):
        convert("13 PM to 2 PM") 

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM") 
    with pytest.raises(ValueError):
        convert("10:99 AM to 2 PM") 

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM") 
