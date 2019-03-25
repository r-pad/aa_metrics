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
    print(t.shape)
    print(x.shape)
    plt.plot(t, x)
    plt.show()

if __name__=="__main__":
    main()
