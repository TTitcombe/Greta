"""
Check carbon intensity before running code
"""
from .errors import CarbonIntensityError
from .query import get_current_intensity, intensity_indices
from .utils import str_to_intensity_enum


def intensity_check_error(limit: str):
    """
    Error code execution if carbon intensity is beyond a threshold

    This func is to be wrapped around another function.
    If carbon intensity is not below the limit,
    code will error.

    Parameters
    ----------
    limit : str
        The maximum carbon intensity index under which the code should run
        (inclusive).
        Must be one of 'very low', 'low', 'moderate', 'high', 'very high'

    Raises
    ------
    greta.CarbonIntensityError
        If carbon intensity index is greater than `limit` upon function execution
    """
    limit_enum = str_to_intensity_enum(limit)

    def outer_func(func):
        def inner_func(*args, **kwargs):
            carbon_intensity_index = get_current_intensity()

            if carbon_intensity_index.value > limit_enum.value:
                raise CarbonIntensityError(
                    f"Carbon intensity is '{carbon_intensity_index.name}', which breaks limit '{limit}'"
                )

            return func(*args, **kwargs)

        return inner_func

    return outer_func


def intensity_check_skip(limit: str):
    """
    Skip code execution if carbon intensity is beyond a threshold

    This func is to be wrapped around another function.
    If carbon intensity is not below the limit,
    the wrapped function will not run and "None" will be returned.

    Parameters
    ----------
    limit : str
        The maximum carbon intensity index under which the code should run
        (inclusive).
        Must be one of 'very low', 'low', 'moderate', 'high', 'very high'
    """
    limit_enum = str_to_intensity_enum(limit)

    def outer_func(func):
        def inner_func(*args, **kwargs):
            carbon_intensity_index = get_current_intensity()

            if carbon_intensity_index.value > limit_enum.value:
                return
            else:
                return func(*args, **kwargs)

        return inner_func

    return outer_func
