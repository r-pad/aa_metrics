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

from aa_metrics.utils import parse_bag

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str,
            help="Path to rosbag")
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    bag = rosbag.Bag(args.file)
    t, x, y, yaw, x_dot, y_dot, yaw_dot, steer, vel = parse_bag(bag)
    plt.ion()

    fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
    ax1.plot(t, x)
    ax1.set_title('Values of x and y Over Time')
    ax2.plot(t, y)
    fig.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)

    fig = plt.figure()
    plt.plot(t, yaw)
    plt.xlabel('Time')
    plt.ylabel('Yaw (rad)')
    plt.title('Value of yaw Over Time')

    fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
    ax1.plot(t, x_dot)
    ax1.set_title('Values of x_dot and y_dot Over Time')
    ax2.plot(t, y_dot)
    fig.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)

    fig = plt.figure()
    plt.plot(t, yaw)
    plt.xlabel('Time')
    plt.ylabel('Yaw Rate (rad)')
    plt.title('Value of yaw_dot Over Time')

    fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
    ax1.plot(t, steer)
    ax1.set_title('Values of Steering and Velocity Commands Over Time')
    ax2.plot(t, vel)
    fig.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)

    fig = plt.figure()
    r = 10*np.sqrt(x_dot**2 + y_dot**2)
    plt.quiver(x, y, r*np.cos(yaw), r*np.sin(yaw))
    plt.title('Trajectory')
    plt.xlabel('x (m)')
    plt.ylabel('x (m)')
    ax1 = plt.gca()
    ax1.axis('equal')

    plt.show()
    sys.stdout.write('Press <enter> to continue: ')
    raw_input()
    return

if __name__=="__main__":
    main()
