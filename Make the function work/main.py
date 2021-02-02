def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    elif remainder != 0:
        a = x - remainder
        return a + 5
