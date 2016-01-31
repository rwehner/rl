def make_bricks(small, big, goal):
    if goal < (big * 5):
        quotient, remainder = divmod(goal, 5)
        if quotient <= big:
            if goal - (quotient * 5) <= small:
                return True
            else:
                return False
    if goal - (big * 5) <= small:
        return True
    return False


def lone_sum(a, b, c):
    orig_values = [a, b, c]
    nondup_values = list()
    for val in orig_values:
        if orig_values.count(val) == 1:
            nondup_values.append(val)
    return sum(nondup_values)
