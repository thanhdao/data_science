# kmean.py
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def kmeans(dataset, k):
  features_num = dataset.get_features_num()
  centroids = get_random_centroids(features_num, k)

  iterations = 0
  old_centroids = None

  while not should_stop(old_centroids, centroids, iterations):

    old_centroids = centroids
    iterations += 1

    labels = get_labels(dataset, centroids)

    centroids = get_centroids(dataset, labels, k)

  return centroids

def get_features_num(dataset):
  return dataset.shape[1]

def get_random_centroids(data, k=3):

  # Number of training data
  n = data.shape[0]
  # Number of features in the data
  
  c = data.shape[1]

  # Generate random centers, here we use sigma and mean to ensure it represent the whole data
  mean = np.mean(data, axis = 0)
  std = np.std(data, axis = 0)
  centers = np.random.randn(k,c)*std + mean

  return centers

def get_labels(dataset, centroids):

  labels = {}

  return labels

def get_centroids(data, k=3):
  # Number of training data
  n = data.shape[0]
  # Number of features in the data
 
  c = data.shape[1]

  centers = get_random_centroids(data, k)
  centers_old = np.zeros(centers.shape) # to store old centers
  centers_new = deepcopy(centers) # Store new centers

  data.shape
  clusters = np.zeros(n)
  distances = np.zeros((n,k))

  error = np.linalg.norm(centers_new - centers_old)

  # When, after an update, the estimate of that center stays the same, exit loop
  while error != 0:

      for i in range(k):
          distances[:,i] = np.sqrt(np.sum(np.square(data - centers[i]), axis = 1))
      # Assign all training data to closest center
      clusters = np.argmin(distances, axis = 1)
      
      centers_old = deepcopy(centers_new)
      # Calculate mean for every cluster and update the center
      for i in range(k):
          centers_new[i] = np.mean(data[clusters == i], axis=0)
      # error = np.linalg.norm(centers_new - centers_old)
      
      error = np.sqrt(np.sum(np.square(centers_new - centers_old))) 

  return centers_new

def should_stop(old_centroids, centroids):
  return old_centroids == centroids

