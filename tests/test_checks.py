"""
Unit tests for greta/checks.py
"""
import pytest
import responses

from greta import check_intensity
from greta.errors import CarbonIntensityError


@check_intensity("low")
def inner_test():
    return "has run"


@responses.activate
def test_code_runs_if_at_threshold_intensity():
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": "low"}}]},
        status=200,
    )

    assert inner_test() == "has run"


@responses.activate
def test_code_runs_if_below_threshold_intensity():
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": "very low"}}]},
        status=200,
    )

    assert inner_test() == "has run"


@responses.activate
@pytest.mark.parametrize("index", ["moderate", "high", "very high"])
def test_code_raises_if_above_threshold_intensity(index):
    responses.add(
        responses.GET,
        "https://api.carbonintensity.org.uk/intensity",
        json={"data": [{"intensity": {"index": index}}]},
        status=200,
    )

    with pytest.raises(CarbonIntensityError):
        inner_test()
