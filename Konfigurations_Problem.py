'''
This module provides functions to generate random points,
calculate distances between them, and visualize the points with connecting lines.
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
    positions[:, 0] = radius * np.cos(angles)+0.5
    positions[:, 1] = radius * np.sin(angles)+0.5
    return positions

def random_line_points(number_of_points, scale=1, offset=[0, 0]):
    '''
    Generate random points in the shape of a line on the x-axis.
    Args:
        number_of_points (int): Number of random points to generate.
        scale (float): Scale factor for the line length.
        offset (array): 2D array of offset to shift the line position.
    Returns:
        array: 2D array containing x and y coordinates of the points.
    '''
    positions = np.random.rand(number_of_points, 2)*[1, 0]*scale+offset
    return positions

def distance_calculation(positions1, positions2):
    '''
    Calculate distances between each point in set1 and each point in set2.
    Args:
        positions (array): 2D array of x and y coordinates.
    Returns:
        array: 2D array of pairwise distances.
    '''
    distance = np.sqrt(np.sum((positions1[:,None,:] - positions2[None,:,:])**2, axis = 2))
    return distance

def plot_points(positions1, positions2):
    '''
    Plot two sets of points and connect each point in set1 with each point in set2.
    Args:
        positions (array): 2D Array of x and y coordinates.
    Returns:
        None
    '''
    plt.figure()
    for i in range(positions1.shape[0]):
        for j in range(positions2.shape[0]):
            plt.plot([positions1[i, 0], positions2[j, 0]], [positions1[i, 1], positions2[j, 1]], color='red')
    plt.scatter(positions1[:, 0], positions1[:, 1], color='blue')
    plt.scatter(positions2[:, 0], positions2[:, 1], color='green')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return


points1 = random_circle_points(10)
points2 = random_line_points(5, offset=[0, -1])
print(distance_calculation(points1, points2))
plot_points(points1, points2)
