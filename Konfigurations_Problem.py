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
        tuple: Two arrays containing x and y coordinates of the points.
    '''
    x_positions = np.random.rand(1,number_of_points)
    y_positions = np.random.rand(1,number_of_points)
    return x_positions, y_positions

def random_circle_points(number_of_points):
    '''
    Generate random points in 2D space, roughly in the shape of a circle. 
    Args:
        number_of_points (int): Number of random points to generate.
    Returns:
        tuple: Two arrays containing x and y coordinates of the points.
    '''
    radius = 0.45 + 0.05 * np.random.rand(number_of_points)
    angles = np.random.rand(number_of_points) * 2 * np.pi

    x_positions = radius * np.cos(angles).reshape(1, number_of_points)
    y_positions = radius * np.sin(angles).reshape(1, number_of_points)
    return x_positions, y_positions

def distance_calculation(x_positions, y_positions):
    '''
    Calculate pairwise distances between points.  
    Args:
        x_positions (array): Array of x coordinates.
        y_positions (array): Array of y coordinates.  
    Returns:
        array: 2D array of pairwise distances.
    '''
    x_distance = np.triu(x_positions.T - x_positions)
    y_distance = np.triu(y_positions.T - y_positions)
    # x_distance = np.triu(np.tile(x_positions.T, (1 , x_positions.shape[1])), k=1) - np.triu(np.tile(x_positions, (x_positions.shape[1], 1)), k=1)
    # y_distance = np.triu(np.tile(y_positions.T, (1 , y_positions.shape[1])), k=1) - np.triu(np.tile(y_positions, (y_positions.shape[1], 1)), k=1)
    
    distance = np.sqrt(x_distance**2 + y_distance**2)
    return distance

def plot_points(x, y):
    ''' 
    Plot points and connect them with lines.
    Args:   
        x (array): Array of x coordinates.
        y (array): Array of y coordinates.
    Returns:
        None
    '''
    plt.figure()
    for i in range(x.shape[1]):
        for j in range(i+1, x.shape[1]):
            plt.plot([x[0,i], x[0,j]], [y[0,i], y[0,j]], color="red")
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return

points = random_circle_points(5)
print(distance_calculation(*points))
plot_points(*points)