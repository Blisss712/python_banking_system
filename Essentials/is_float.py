def is_float(s):
    """
    Checks if a string can be successfully converted to a float.

    Args:
    s: The string to check.

    Returns:
    bool: True if the string can be converted to a float, False otherwise.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False