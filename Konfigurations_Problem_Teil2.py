'''
Konfigurations_Problem_Teil2.py
This script generates two sets of points in 2D space: one set arranged in a circle
and another set arranged in a grid. It calculates the pairwise distances between the points 
from both sets and visualizes the shortest distances from the grid points to the circle points
as a heatmap. The circle points are plotted on top of the heatmap for reference.
'''

import numpy as np
import matplotlib.pyplot as plt

def circle_points(number_of_points, offset=(0, 0)):
    '''
    Generate points in 2D space, in the shape of a circle.
    Args:
        number_of_points (int): Number of points to generate.
    Returns:
        array: 2D array containing x and y coordinates of the points.
    '''
    radius = 3
    angles = np.linspace(2*np.pi/number_of_points, 2*np.pi, number_of_points)
    positions = np.empty((number_of_points, 2))
    positions[:, 0] = radius * np.cos(angles)
    positions[:, 1] = radius * np.sin(angles)
    positions += np.array(offset)
    return positions

def grid_points(nx, ny):
    '''
    Generate grid points in 2D space.
    Args:
        nx (int): Number of points in x direction.
        ny (int): Number of points in y direction.
    Returns:
        array: 2D array containing x and y coordinates of the points.
    '''
    # Meshgrid approach (alternative)
    # xx, yy = np.meshgrid(np.linspace(0, 10, num=nx), np.linspace(0, 10, num=ny))
    # positions = np.empty((nx*ny, 2))
    # positions[:, 0] = xx.flatten()
    # positions[:, 1] = yy.flatten()

    positions = np.empty((nx*ny, 2))
    positions[:, 0] = np.tile(np.linspace(0, 10, num=nx), ny)
    positions[:, 1] = np.repeat(np.linspace(0, 10, num=ny), nx)
    return positions

def distance_calculation(positions1, positions2):
    '''
    Calculate distances between each point in set1 and each point in set2.
    Args:
        positions (array): 2D array of x and y coordinates.
    Returns:
        array: 2D array of pairwise distances.
    '''
    distance = np.sqrt(np.sum((positions1[:, None, :] - positions2[None, :, :])**2, axis=2))
    return distance

def shortest_distance(distance):
    '''
    Calculate the shortest distance from the points of set2 to any point in set1.
    Args:
        distance (array): 2D array of pairwise distances between points of set1 and set2.
    Returns:
        array: 1D array with shortest distance from the points in set2 to any point in set1
    '''
    return np.min(distance, axis=0)

def plot_distance(positions1, positions2, shortest_dist, nx, ny):
    '''
    Plot the grid set2 as a heatmap with the color corresponding to the distance to set1. 
    Also plot the points of set1 on top of the heatmap. 
    Args:
        positions1 (array): 2D array of x and y coordinates of set1.
        positions2 (array): 2D array of x and y coordinates of set2.
        shortest_dist (array): 1D array with shortest distances from set2 to set1.
        nx (int): Number of points in x direction for set2.
        ny (int): Number of points in y direction for set2.
    Returns:
        None
    '''
    grid = np.reshape(shortest_dist, shape=(ny, nx))
    x_min = np.min(positions2[:, 0])
    x_max = np.max(positions2[:, 0])
    y_min = np.min(positions2[:, 1])
    y_max = np.max(positions2[:, 1])
    plt.imshow(grid, extent=[x_min, x_max, y_min, y_max], origin='lower')
    plt.colorbar()
    plt.scatter(positions1[:, 0], positions1[:, 1], color='red')
    plt.show()
    return


n_circ = 5
n_x = 100
n_y = 40
points1 = circle_points(n_circ, offset=(5, 5))
points2 = grid_points(n_x, n_y)
dist = distance_calculation(points1, points2)

plot_distance(points1, points2, shortest_distance(dist), n_x, n_y)
