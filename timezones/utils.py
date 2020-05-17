from django.conf import settings


def clean_setting(
    name: str,
    default_value: object,
    min_value: int = None,
    max_value: int = None,
    required_type: type = None
):
    """cleans the input for a custom setting

    Will use `default_value` if settings does not exit or has the wrong type
    or is outside define boundaries (for int only)

    Need to define `required_type` if `default_value` is `None`

    Will assume `min_value` of 0 for int (can be overriden)

    Returns cleaned value for setting
    """
    if default_value is None and not required_type:
        raise ValueError('You must specify a required_type for None defaults')

    if not required_type:
        required_type = type(default_value)

    if min_value is None and required_type == int:
        min_value = 0

    if not hasattr(settings, name):
        cleaned_value = default_value
    else:
        if (isinstance(getattr(settings, name), required_type)
            and (min_value is None or getattr(settings, name) >= min_value)
            and (max_value is None or getattr(settings, name) <= max_value)
        ):
            cleaned_value = getattr(settings, name)
        else:
            logger.warn(
                'You setting for {} it not valid. Please correct it. '
                'Using default for now: {}'.format(
                    name,
                    default_value
                )
            )
            cleaned_value = default_value
    return cleaned_value
