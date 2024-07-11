"""
Miscellaneous string functions
"""

def prefix(s1: str, s2: str) -> tuple[str, str, str]:
    """
    Compute the common prefix of two strings.

    Args:
        `s1`: first string
        `s2`: second string

    Returns:
        (str, str, str): common prefix, remaining s1, remaining s2
    
    RT: O(min(n, m))
        n = len(s1)
        m = len(s2)
    SC: O(1)
    """
    i = 0

    for a, b in zip(s1, s2):
        if a != b:
            break
        i += 1
    
    return s1[:i], s1[i:], s2[i:]