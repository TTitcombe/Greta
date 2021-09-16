"""
Unit tests for greta/variables.py
"""
import pytest
import responses

from greta import condition_variable


@responses.activate
def test_variable_takes_first_value_if_at_threshold_intensity():
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": "low"}}]},
        status=200,
    )

    actual_variable = condition_variable(1.0, -1.0, "low")
    assert actual_variable == 1.0


@responses.activate
def test_variable_takes_first_value_if_below_threshold_intensity():
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": "very low"}}]},
        status=200,
    )

    actual_variable = condition_variable(1.0, -1.0, "low")
    assert actual_variable == 1.0


@responses.activate
@pytest.mark.parametrize("index", ["moderate", "high", "very high"])
def test_variable_takes_first_value_if_above_threshold_intensity(index):
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": index}}]},
        status=200,
    )

    actual_variable = condition_variable(1.0, -1.0, "low")
    assert actual_variable == -1.0
