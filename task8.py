import numpy as np
import matplotlib.pyplot as plt

def bezier_curve(control_points, num_points=100):
    """
    Draws a Bezier curve with the given control points.
    """
    t = np.linspace(0, 1, num_points)
    curve = np.zeros((num_points, 2))
    for i in range(num_points):
        curve[i] = (1-t[i])**3 * control_points[0] + 3*(1-t[i])**2*t[i] * control_points[1] + 3*(1-t[i])*t[i]**2 * control_points[2] + t[i]**3 * control_points[3]
    return curve

def draw_bezier_curve(control_points):
    curve = bezier_curve(control_points)
    x, y = curve.T
    plt.plot(x, y, 'b-')
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro')
    plt.show()

control_points = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
draw_bezier_curve(control_points)
