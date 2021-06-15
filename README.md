# PI-Estimate
Estimate PI, using random[0,1]

This program estimates pi using only random number generation from 0 to 1.
Random points are generated, then it is checked whether they are included in the unit circle.
The ratio of the number of points in a circle to the total number of points allows you
to estimate the area of the circle.
The area of the unit circle is pi.

area = PI*r^2

(pi*r^2)/(2*r^2) = in_circle_points/all_points
pi = (4*in_circle_points)/all_points




16.06.2021

Python 3.9.4

Package: random, math, matplotlib
