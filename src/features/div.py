def div(a, b):
    if a == 0 or b == 0:
        return None

    if a < 0 and b < 0:
        return None
    else:
        return a / b