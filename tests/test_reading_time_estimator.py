from lib.reading_time_estimator import *
"""
Given an empty string
It returns 0
estimate_reading_time("") => 0.0

"""
def test_estimate_reading_time_returns_0_for_empty_string():
    result = estimate_reading_time("")
    assert result == 0