'''
Konfigurations_Problem_Teil2.py
This script generates random points in a circular configuration and grid points in 2D space.
It calculates pairwise distances between the two sets of points, finds the shortest distance
from a specific grid point to the other grid and identifies the closest point.
Finally, it visualizes the distances from a given point in a heatmap.
'''

import numpy as np
import matplotlib.pyplot as plt

def random_circle_points(number_of_points, offset=[0, 0]):
    '''
    Generate random points in 2D space, in the shape of a circle.
    Args:
        number_of_points (int): Number of random points to generate.
    Returns:
        array: 2D array containing x and y coordinates of the points.
    '''
    radius = 3
    angles = np.random.rand(number_of_points) * 2 * np.pi
    positions = np.empty((number_of_points, 2))
    positions[:, 0] = radius * np.cos(angles)
    positions[:, 1] = radius * np.sin(angles)
    positions += offset
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

def grid_point_number(x_number, y_number, nx):
    '''
    Calculate the index of a disired point in the positions matrix from its x and y indices.
    Indices start at 0. Necessary because grid points are stored in an array of dimension (nx*ny,2).
    Args:
        x_number (int): x index of the point.
        y_number (int): y index of the point.
        nx (int): number of points in x direction.
    Returns:
        int: index of the desired point.
    '''
    return x_number + nx*y_number

def shortest_distance(point_number, distance):
    '''
    Calculate the shortest distance from a given point of set2 to all points in set1.
    Args:
        point_number (int): index of point in set2 to calculate distances from.
        distance (array): 2D array of pairwise distances between points of set1 and set2.
    Returns:
        float: shortest distance from the given point to set1.
    '''
    return np.min(distance[:, point_number])

def closest_point(point_number, distance):
    '''
    Calculate the index of the point in set1 that is closest to a given point in set2.
    Args:
        point_number (int): point number in set2 to calculate distances from.
        distance (array): 2D array of pairwise distances between points of set1 and set2.
    Returns:
        int: index of point in set1 that is closest to the given point in set2.
    '''
    return np.argmin(distance[:, point_number])

def plot_distance(positions1, positions2, centerpoint, close_point):
    '''
    Plot the distances from a given point in set2 in a heatmap.
    Plot also shows the points of both sets, highlighting the given point in set2 and the closest point in set1.
    Args:
        positions1 (array): 2D array of x and y coordinates of set1.
        positions2 (array): 2D array of x and y coordinates of set2.
        centerpoint (array): x and y coordinates of the point in set2 to calculate distances from.
        close_point (int): index of the point in set1 that is closest to the given point in set2.
    Returns:
        None
    '''
    x_min = min(0, np.min(positions1[:, 0]))-1
    x_max = max(10, np.max(positions1[:, 0]))+1
    y_min = min(0, np.min(positions1[:, 1]))-1
    y_max = max(10, np.max(positions1[:, 1]))+1

    x = np.linspace(x_min, x_max, num=100)
    y = np.linspace(y_min, y_max, num=100)
    z = np.sqrt((x-centerpoint[0])[None, :]**2 + (y-centerpoint[1])[:, None]**2)

    plt.imshow(z, extent=[x_min, x_max, y_min, y_max], origin='lower')

    plt.scatter(positions2[:, 0], positions2[:, 1], color='green')
    plt.scatter(centerpoint[0], centerpoint[1], color='red')
    plt.scatter(positions1[:, 0], positions1[:, 1], color='blue')
    plt.scatter(positions1[close_point, 0], positions1[close_point, 1], color='red')

    plt.show()
    return


n_circ = 10
n_x = 10
n_y = 3
points1 = random_circle_points(n_circ, offset=[5, 14])
points2 = grid_points(n_x, n_y)

dist = distance_calculation(points1, points2)
point_numb = grid_point_number(7, 1, n_x)
print(shortest_distance(point_numb, dist))
c_point = closest_point(point_numb, dist)

plot_distance(points1, points2, points2[point_numb], c_point)
