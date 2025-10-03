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
    radius = 0.9 + 0.1 * np.random.rand(number_of_points)
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
    x_distance = x_positions.T - x_positions
    y_distance = y_positions.T - y_positions
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
    x = x.flatten()
    y = y.flatten()
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            plt.plot([x[i], x[j]], [y[i], y[j]], color="red")
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return

points = random_circle_points(10)
print(distance_calculation(*points))
plot_points(*points)
