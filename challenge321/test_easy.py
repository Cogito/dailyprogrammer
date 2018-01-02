from easy import *


def test_time_talking():
    test_cases = (
        ("00:00", "It's twelve am"),
        ("01:30", "It's one thirty am"),
        ("12:05", "It's twelve oh five pm"),
        ("14:01", "It's two oh one pm"),
        ("20:29", "It's eight twenty nine pm"),
        ("21:00", "It's nine pm"),
    )
    for (case, expected) in test_cases:
        assert time_to_text(case) == expected
