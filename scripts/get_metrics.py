#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: edwardahn

Evaluate metrics for real data collected from a rosbag.
"""

import argparse
import os
import sys
sys.path.append(os.getcwd())

import matplotlib.pyplot as plt
import numpy as np
import rosbag

from aa_metrics.plot import *
from aa_metrics.utils import parse_bag


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
            help="Path to rosbag")
    parser.add_argument('--circle', dest='is_circle',
            action='store_true', help='Additional plots for circle')
    parser.add_argument('--no-circle', dest='is_circle',
            action='store_false', help='Additional plots for circle')
    parser.set_defaults(is_circle=False)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    bag = rosbag.Bag(args.file)
    t, x, y, yaw, x_dot, y_dot, yaw_dot, steer, vel = parse_bag(bag)
    plt.ion()

    data = [x, y]
    names = ['x', 'y']
    units = ['m', 'm']
    plot_two_curves(t, data, names, units)

    data = yaw
    name = 'Yaw'
    units = 'rad'
    plot_curve(t, data, name, units)

    data = [x_dot, y_dot]
    names = ['x Rate', 'y Rate']
    units = ['m/s', 'm/s']
    plot_two_curves(t, data, names, units)

    data = yaw_dot
    name = 'Yaw Rate'
    units = 'rad'
    plot_curve(t, data, name, units)

    data = [steer, vel]
    names = ['Commanded Steering', 'Commanded Velocity']
    units = ['rad', 'm/s']
    plot_two_curves(t, data, names, units)

    plt.figure()
    yaw = np.pi*yaw
    u = x_dot*np.cos(yaw) - y_dot*np.sin(yaw)
    v = x_dot*np.sin(yaw) + y_dot*np.cos(yaw)
    plt.quiver(x, y, u, v)
    plt.title('Trajectory')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    ax1 = plt.gca()
    ax1.axis('equal')

    speeds = np.sqrt(x_dot**2 + y_dot**2)
    name = 'Measured Speeds'
    units = 'm/s'
    plot_distribution(speeds, name, units)

    if args.is_circle:
        r = 1
        distance_errors = r - np.sqrt(np.square(x) + np.square(y))
        data = distance_errors
        name = 'Distance Errors'
        units = 'm'
        plot_curve(t, data, name, units)
        plot_distribution(data, name, units)

    plt.show()
    sys.stdout.write('Press <enter> to continue: ')
    raw_input()
    return


if __name__=="__main__":
    main()
