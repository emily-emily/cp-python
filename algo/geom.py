def dist(x1, y1, x2, y2) -> float:
    """
    Finds the Euclidean distance between two points.

    Args:
    - x1, y1: first point
    - x2, y2: second point

    Returns: Euclidean distance between the two points
    """
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def intersect(x1, y1, r1, x2, y2, r2) -> bool:
    """
    Determines whether two circles intersect.

    Args:
    - x1, y1: center of first circle
    - r1: radius of first circle
    - x2, y2: center of second circle
    - r2: radius of second circle

    Returns: whether the two circles intersect

    We can check the distance between the two centers and compare it to the sum of the radii.
    Note that we do not need to sqrt the distance because both sides are squared.
    """
    return (x1 - x2)**2 + (y1 - y2)**2 <= (r1 + r2)**2
