'''
This module provides functions to generate random points in 2D space,
calculate pairwise distances between them, and visualize the points with connecting lines.
'''

import numpy as np
import matplotlib.pyplot as plt

def random_points(number_of_points):
    '''
    Generate random points in 2D space.
    Args:
        number_of_points (int): Number of random points to generate.
    Returns:
        array: 2D array containing x and y coordinates of the points.
    '''
    positions = np.random.rand(number_of_points, 2)
    return positions

def random_circle_points(number_of_points):
    '''
    Generate random points in 2D space, roughly in the shape of a circle. 
    Args:
        number_of_points (int): Number of random points to generate.
    Returns:
        array: 2D array containing x and y coordinates of the points.
    '''
    radius = 0.45 + 0.05 * np.random.rand(number_of_points)
    angles = np.random.rand(number_of_points) * 2 * np.pi
    positions = np.empty((number_of_points, 2))
    positions[:, 0] = radius * np.cos(angles)
    positions[:, 1] = radius * np.sin(angles)
    return positions

def distance_calculation(positions):
    '''
    Calculate pairwise distances between points.
    Args:
        positions (array): 2D array of x and y coordinates.
    Returns:
        array: 2D array of pairwise distances.
    '''
    # x_distance = x_positions.T - x_positions
    # y_distance = y_positions.T - y_positions
    # distance = np.sqrt(x_distance**2 + y_distance**2)
    distance = np.sqrt((positions.T[:1]-positions[:, :1])**2 + (positions.T[1:]-positions[:, 1:])**2)
    return distance

def plot_points(positions):
    '''
    Plot points and connect them with lines.
    Args:
        positions (array): 2D Array of x and y coordinates.
    Returns:
        None
    '''
    plt.figure()
    for i in range(positions.shape[0]):
        for j in range(i+1, positions.shape[0]):
            plt.plot([positions[i, 0], positions[j, 0]], [positions[i, 1], positions[j, 1]], color="red")
    plt.scatter(positions[:, 0], positions[:, 1])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return

points = random_circle_points(5)
print(points)
print(distance_calculation(points))
plot_points(points)
