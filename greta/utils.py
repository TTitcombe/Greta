from .query import IntensityIndex, intensity_indices


def str_to_intensity_enum(str_intensity: str) -> IntensityIndex:
    """
    Convert a string to an intensity enum

    Parameters
    ----------
    str_intensity : str
        The intensity level in words

    Returns
    -------
    IntensityIndex
        The intensity level as an enum

    Raises
    ------
    ValueError
        If `str_intensity` is not one of
        'very low', 'low', 'moderate', 'high', 'very high'

    """
    if str_intensity not in intensity_indices:
        raise ValueError(
            f"{str_intensity} is not a valid carbon intensity index."
            "Must be one of 'very low', 'low', 'moderate', 'high', 'very high'"
        )

    return intensity_indices[str_intensity]
