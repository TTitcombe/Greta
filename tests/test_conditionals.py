"""
Unit tests for greta/variables.py
"""
import pytest
import responses

from greta import condition_function, condition_variable


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


def func1():
    return "low"


def func2():
    return "high"


@responses.activate
def test_function_runs_if_below_threshold_intensity():
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": "very low"}}]},
        status=200,
    )

    actual_result = condition_function(func1, func2, "low")
    assert actual_result == "low"


@responses.activate
def test_function_runs_if_at_threshold_intensity():
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": "low"}}]},
        status=200,
    )

    actual_result = condition_function(func1, func2, "low")
    assert actual_result == "low"


@responses.activate
@pytest.mark.parametrize("index", ["moderate", "high", "very high"])
def test_function_runs_if_above_threshold_intensity(index):
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": index}}]},
        status=200,
    )

    actual_result = condition_function(func1, func2, "low")
    assert actual_result == "high"


@responses.activate
def test_function_can_take_arguments():
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": "very low"}}]},
        status=200,
    )

    def inner_func1(var1, var2):
        return var1 + var2

    def inner_func2(var1, var2):
        return 0 - var1 - var2

    actual_result = condition_function(inner_func1, inner_func2, "low", 5, 6)
    assert actual_result == 11
