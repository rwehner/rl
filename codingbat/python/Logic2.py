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
