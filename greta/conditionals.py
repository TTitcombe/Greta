"""
Altering variables and values
conditional on carbon intensity
"""
from typing import Callable

from .query import get_current_intensity
from .utils import str_to_intensity_enum


def condition_variable(low_value, high_value, limit: str):
    """
    Set a value conditional on carbon intensity

    If carbon intensity is below or equal to a given threshold,
    the `low_value` is given; otherwise `high_value` is given

    Parameters
    ----------
    low_value : <T>
        The value to return if carbon intensity is at or below
        `limit`
    high_value : <T>
        The value to return if carbon intensity is above
        `limit`
    limit : str
        The carbon intensity on which the values are conditioned

    Returns
    -------
    <T>
        `low_value` or `high_value`
    """
    limit_enum = str_to_intensity_enum(limit)
    carbon_intensity_index = get_current_intensity()

    if carbon_intensity_index.value <= limit_enum.value:
        return low_value
    else:
        return high_value


def condition_function(
    low_func: Callable, high_func: Callable, limit: str, *args, **kwargs
):
    """
    Run a particular function based on carbon intensity

    Given two functions (one to be run at low intensity and one at high),
    select which one to execute at runtime based on the current
    carbon intensity

    Parameters
    ----------
    low_func : function
        Function to be executed if intensity is at or below `limit`
    high_func : function
        Function to be executed if intensity is above `limit`
    limit : str
        The carbon intensity on which the values are conditioned
    *args
        args for the functions
    **kwargs
        kwargs for the functions
    """
    limit_enum = str_to_intensity_enum(limit)
    carbon_intensity_index = get_current_intensity()

    func = low_func if carbon_intensity_index.value <= limit_enum.value else high_func

    return func(*args, **kwargs)
