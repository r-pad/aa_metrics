#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: edwardahn

Functions for plotting data.
"""

import matplotlib.pyplot as plt


def plot_curve(t, data, name, units):
    """
    Plot one curve over time.
    """
    plt.figure()
    plt.plot(t, data)
    plt.xlabel('Time (ns)')
    plt.ylabel('%s (%s)' % (name, units))
    plt.title('Value of %s Over Time' % name)


def plot_two_curves(t, data, names, units):
    """
    Plot two curves on subplot sharing same x and y-axis over time.
    """
    data1 = data[0]
    data2 = data[1]
    fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
    ax1.plot(t, data1)
    ax1.set_ylabel('%s (%s)' % (names[0], units[0]))
    ax1.set_title('Values of %s and %s Over Time' % (names[0], names[1]))
    ax2.plot(t, data2)
    ax2.set_ylabel('%s (%s)' % (names[1], units[1]))
    ax2.set_xlabel('Time (ns)')
    fig.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)


def plot_distribution(data, name, units):
    """
    Plot histogram showing distribution of data.
    """
    mean = data.mean()
    std = data.std()
    maximum = data.max()
    minimum = data.min()
    stats = 'Mean = %.5f\nStd = %.5f\nMax = %.5f\nMin = %.5f' % \
            (mean, std, maximum, minimum)
    title = 'Distribution of %s in Final Policy' % name

    plt.figure()
    plt.hist(data)
    plt.title(title)
    plt.xlabel('%s (%s)' % (name, units))
    plt.ylabel('Number of Time Steps (ns)')
    plt.axvline(mean, color='k', linestyle='dashed', linewidth=1)
    plt.axvline(mean+std, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(mean-std, color='r', linestyle='dashed', linewidth=1)
    plt.text(0.87, 0.9, stats, ha='center', va='center',
            transform=plt.gca().transAxes)
