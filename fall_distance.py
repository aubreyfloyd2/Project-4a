# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/30/2023
# Description: Function to give the distance an object falls due to gravity
#              in a specific time period.

def fall_distance(t):
    """Returns the distance an object falls due to gravity in a specific time period"""
    result = ((.5) * 9.8 * (t ** 2))
    return result

# dist = fall_distance(3.2)
# print(dist)