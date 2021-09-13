"""
Functions for checking carbon intensity
from an API
"""
from enum import Enum

import requests

UK_URL = "https://api.carbonintensity.org.uk/intensity"


class IntensityIndex(Enum):
    very_low = 0
    low = 1
    moderate = 2
    high = 3
    very_high = 4


intensity_indices = {
    "very low": IntensityIndex.very_low,
    "low": IntensityIndex.low,
    "moderate": IntensityIndex.moderate,
    "high": IntensityIndex.high,
    "very high": IntensityIndex.very_high,
}


def get_current_intensity() -> str:
    """
    Get the current carbon intensity for the UK
    from carbonintensity.org API.

    Returns
    -------
    str
        Carbon intensity "index": one of
        'very low', 'low', 'moderate', 'high', 'very high'
    """
    data = requests.get(UK_URL).json()["data"][0]["intensity"]
    return intensity_indices[data["index"]]
