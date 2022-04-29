"""
Contains function for plotting.
"""
import matplotlib.pyplot as plt

from entity.Config import *


def plot(data : dict, name : str = None):
    """
    params:
    - data: {
        (x, y): [utility for each iteration (float)]
    }
    - name (str): name of file to save plot as; defaults to None (not saved)
    """
    plt.figure(figsize=(16, 8))

    for key in data:
        plt.plot(data[key])

    plt.legend(data, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.title(name)
    plt.xlabel('Number of Iteration')
    plt.ylabel('Utility')

    # Need to save first before plot show
    if name is not None:
        plt.savefig("./" + name + ".png")
    plt.show()


