def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move at the same speed. Two cars collide when a car moving
    left to right meets a car moving right to left. However, the cars are infinitely
    sturdy and strong; as a result, they continue moving in their trajectory as if
    they did not collide.

    This function outputs the total number of collisions.
    """
    return n * n