"""
Estimate PI, using random[0,1]

This program estimates pi using only random number generation from 0 to 1.
Random points are generated, then it is checked whether they are included in the unit circle.
The ratio of the number of points in a circle to the total number of points allows you
to estimate the area of the circle.
The area of the unit circle is pi.
area = PI*r^2

"""

import random
import math
import matplotlib.pyplot as plt


def estimate(n, visual=False):
    in_circle_points = 0
    all_points = 0
    points = []
    for _ in range(n):
        x = random.random()
        y = random.random()
        points.append((x, y))
        all_points += 1
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            in_circle_points += 1
    if visual:
        visualization(points)
    return 4.0*in_circle_points/all_points


def visualization(points):
    circle = plt.Circle((0, 0), 1, color='r', fill=False)
    plt.gca().add_artist(circle)
    plt.scatter([x[0] for x in points], [y[1] for y in points], alpha=0.5)
    plt.show()


if __name__ == '__main__':
    print(estimate(1000, True))
    print(estimate(10000))
    print(estimate(100000))
    print(estimate(1000000))
