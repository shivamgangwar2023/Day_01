import numpy as np;
import matplotlib.pyplot as plt;
from matplotlib.colors import ListedColormap

def load_data():
    X = np.load("data/ex7_X.npy")
    return X

def draw_line(p1,p2):
    plt.plot([p1[0],p2[0]],[p1[1],p2[1]])

def plot_data_points(X,idx):
    # X is the set of data points
    # idx contains the centroid assigned to each data point

    cmap=ListedColormap(['Red','Green','Blue'])
    c=cmap(idx)
    plt.scatter(X[:,0],X[:,1],edgecolors=c,alpha=0.69)

def plot_progress_kMeans(X, centroids, previous_centroids, idx, K, i):
    # Plot the examples
    plot_data_points(X, idx)
    
    # Plot the centroids as black 'x's
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='k', linewidths=3)
    
    # Plot history of the centroids with lines
    for j in range(centroids.shape[0]):
        draw_line(centroids[j, :], previous_centroids[j, :])
    
    plt.title("Iteration number %d" %i)


 