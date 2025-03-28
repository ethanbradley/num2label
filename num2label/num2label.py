def uppercase_letter(number: int, strict: bool = False) -> str:
    """
    Map an integer number to an uppercase letter.

    This function takes an integer number and maps it to its
    corresponding uppercase letter in the alphabet (e.g., 1 => 'A'). The
    number must be greater than zero. If the number is greater than 26,
    the alphabet is effectlively looped until the corresponding letter
    is reached (e.g., 28 => 'B').

    Parameters:
        number (int, required): The number to map to an uppercase
            letter.
        strict (bool, optional, False): Whether or not to ensure the
            number is less than 27. If True, and the number is greater
            than 26, an error is raised.

    Returns:
        str: The uppercase letter to which the number has been mapped.
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    elif number < 1:
        raise ValueError("Number must be greater than zero.")
    elif strict and number > 26:
        raise ValueError("Number must be between one and 26 (inclusive).")

    return chr((number - 1) % 26 + ord('A'))


def lowercase_letter(number: int, strict: bool = False) -> str:
    """
    Map an integer number to a lowercase letter.

    This function takes an integer number and maps it to its
    corresponding lowercase letter in the alphabet (e.g., 1 => 'a'). The
    number must be greater than zero. If the number is greater than 26,
    the alphabet is effectlively looped until the corresponding letter
    is reached (e.g., 28 => 'b').

    Parameters:
        number (int, required): The number to map to a lowercase letter.
        strict (bool, optional, False): Whether or not to ensure the
            number is less than 27. If True, and the number is greater
            than 26, an error is raised.

    Returns:
        str: The lowercase letter to which the number has been mapped.
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    elif number < 1:
        raise ValueError("Number must be greater than zero.")
    elif strict and number > 26:
        raise ValueError("Number must be between one and 26 (inclusive).")

    return chr((number - 1) % 26 + ord('a'))


def spreadsheet_column(number: int) -> str:
    """
    Map an integer number to a spreadsheet column label.

    This function takes an integer number and maps it to its
    corresponding spreadsheet column label (e.g., 1 => 'A', 27 => 'AA',
    etc.).

    Parameters:
        number (int, required): The number to map to a spreadsheet
            column label.

    Returns:
        str: The spreadsheet column label to which the number has been
            mapped.
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    elif number < 1:
        raise ValueError("Number must be greater than zero.")

    label = ""
    while number > 0:
        number -= 1
        label = chr(number % 26 + ord('A')) + label
        number //= 26

    return label
