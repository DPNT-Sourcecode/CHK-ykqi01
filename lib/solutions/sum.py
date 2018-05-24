# noinspection PyShadowingBuiltins,PyUnusedLocal
def sum(x, y):
    if x > 100 or x < 0:
        raise ValueError("x value out of range")
    if y > 100 or y < 0:
        raise ValueError("y value out of range")

    return x + y