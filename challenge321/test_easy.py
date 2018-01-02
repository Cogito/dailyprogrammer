import pytest
from easy import *

test_data = [
    ("00:00", "It's twelve am"),
    ("01:30", "It's one thirty am"),
    ("12:05", "It's twelve oh five pm"),
    ("14:01", "It's two oh one pm"),
    ("20:29", "It's eight twenty nine pm"),
    ("21:00", "It's nine pm"),
    ("07:17", "It's seven seventeen am"),
    ("13:12", "It's one twelve pm"),
]


@pytest.mark.parametrize("a, expected", test_data)
def test_time_to_text(a, expected):
    assert time_to_text(a) == expected


@pytest.mark.parametrize("a, _", test_data)
def test_speak_time(a, _):
    speak_time(a)
