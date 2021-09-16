"""
Unit tests for greta/checks.py
"""
import pytest
import responses

from greta import intensity_check_error, intensity_check_skip
from greta.errors import CarbonIntensityError


class TestIntensityCheckError:
    @intensity_check_error("low")
    def inner_test(self):
        return "has run"

    @responses.activate
    def test_code_runs_if_at_threshold_intensity(self):
        responses.add(
            responses.GET,
            "https://api.carbonintensity.org.uk/intensity",
            json={"data": [{"intensity": {"index": "low"}}]},
            status=200,
        )

        assert self.inner_test() == "has run"

    @responses.activate
    def test_code_runs_if_below_threshold_intensity(self):
        responses.add(
            responses.GET,
            "https://api.carbonintensity.org.uk/intensity",
            json={"data": [{"intensity": {"index": "very low"}}]},
            status=200,
        )

        assert self.inner_test() == "has run"

    @responses.activate
    @pytest.mark.parametrize("index", ["moderate", "high", "very high"])
    def test_code_raises_if_above_threshold_intensity(self, index):
        responses.add(
            responses.GET,
            "https://api.carbonintensity.org.uk/intensity",
            json={"data": [{"intensity": {"index": index}}]},
            status=200,
        )

        with pytest.raises(CarbonIntensityError):
            self.inner_test()
