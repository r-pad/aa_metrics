#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: edwardahn

Utility functions for reading bag files for the Assured Autonomy
Project.
"""

import numpy as np

def parse_bag(bag):
    start_time = None
    num_messages = bag.get_message_count()
    t = []
    x = []
    y = []
    yaw = []
    x_dot = []
    y_dot = []
    yaw_dot = []
    steer = []
    vel = []

    first_message_read = False
    recorded_topics = ["/ekf_localization/odom", "/commands/keyboard"]
    for topic, msg, ros_t in bag.read_messages(topics=recorded_topics):
        if not first_message_read:
            first_message_read = True
            start_time = 10**9 * ros_t.secs + ros_t.nsecs
        current_time = 10**9 * ros_t.secs + ros_t.nsecs
        index = int(current_time - start_time)
        t.append(current_time)
        if topic == "/ekf_localization/odom/" or \
                topic == "/ekf_localization/odom":
            x.append(msg.pose.pose.position.x)
            y.append(msg.pose.pose.position.y)
            yaw.append(msg.pose.pose.orientation.z)
            x_dot.append(msg.twist.twist.linear.x)
            y_dot.append(msg.twist.twist.linear.y)
            yaw_dot.append(msg.twist.twist.angular.z)

            # Interpolate
            if len(steer) > 0:
                steer.append(steer[-1])
                vel.append(vel[-1])
            else:
                steer.append(0)
                vel.append(0)

        elif topic == "/commands/keyboard/" or \
                topic == "/commands/keyboard":
            steer.append(msg.drive.steering_angle)
            vel.append(msg.drive.speed)

            # Interpolate
            if len(x) > 0:
                x.append(x[-1])
                y.append(y[-1])
                yaw.append(yaw[-1])
                x_dot.append(x_dot[-1])
                y_dot.append(y_dot[-1])
                yaw_dot.append(yaw_dot[-1])
            else:
                x.append(0)
                y.append(0)
                yaw.append(0)
                x_dot.append(0)
                y_dot.append(0)
                yaw_dot.append(0)
        else:
            raise RuntimeError("Unknown message read")

    bag.close()

    t = np.array(t)
    x = np.array(x)
    y = np.array(y)
    yaw = np.array(yaw)
    x_dot = np.array(x_dot)
    y_dot = np.array(y_dot)
    yaw_dot = np.array(yaw_dot)
    steer = np.array(steer)
    vel = np.array(vel)
    return t, x, y, yaw, x_dot, y_dot, yaw_dot, steer, vel
