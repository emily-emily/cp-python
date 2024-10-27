import random

def generate_arr(dimensions: tuple, a: int, b: int) -> list:
    """
    Generate an ND array of dimensions dimensions with random integers in the range [a, b]
    """
    if len(dimensions) == 1:
        return [random.randint(a, b) for _ in range(dimensions[0])]
    ans = []
    for dim in dimensions:
        for _ in range(dim):
            ans.append(generate_arr(dimensions[1:], a, b))
    return ans
