def is_palindrome(text: str) -> bool:
    """Check whether or not a string is a palindrome.

    Args:
        - text: the string to check

    Returns:
        - True if a palindrome, otherwise False.
        
    Examples:
        - "abba" is a palindrome; should return True.
        - "abcd" is not a palindrome; should return False.
    """
    
    halfway = len(text) // 2
    queue = list(text[:halfway])

    if len(text) % 2 == 0:
        second_Half = text[halfway:]
    else:
        second_Half = text[halfway + 1:]

    for c in second_Half:
        if c != queue.pop():
            return False

        
    return True
