# kmean_spec.py
import unittest
from kmean import *

def show_data_centers(dataset, centers):
    # Plot the data and the centers generated as random
    plt.scatter(dataset[:,0], dataset[:,0], s=7)
    plt.scatter(centers[:,0], centers[:,0], marker='*', c='g', s=150)
    plt.show()

class TestKmeans(unittest.TestCase):
  def test_dataset_features(self):
    # print(dataset.shape)
    # self.assertEqual(dataset.shape[1], 2)
    print(std_norm_samples.shape)
    self.assertEqual(std_norm_samples.shape, (1000,1))
    # pass

  def test_random_centroids(self):
    # centers = get_random_centroids(dataset, 3)
    # self.assertEqual(centers.shape[0], 3)

    centroids = get_random_centroids(std_norm_samples, 5)
    print('centroids: ', centroids)
    self.assertEqual(centroids.shape[0], 5)
    # pass

  def test_get_labels(self):
    # self.assertEqual(get_labels, k)
    pass

  def test_get_centroids(self):
    # centroids = get_centroids(dataset)
    # print('update centroids: ', centroids)
    # self.assertEqual(centroids.shape[0], 3)
    # show_data_centers(dataset, centroids)

    centroids = get_centroids(std_norm_samples, 5)
    print('update centroids: ', centroids)
    self.assertEqual(centroids.shape[0], 5)
    show_data_centers(std_norm_samples, centroids)
    
    # pass

  def test_should_stop(self):
    # self.assertEqual(should_stop, True)
    pass


# dataset = mu, sigma = 0., 1. # mean and standard deviation
# s = np.random.normal(mu, sigma, 10)

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([8, 8, 8, 8, 8])
# z = np.ones((5, 9))
# print(z)

# x = [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46]
# y = [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
# dataset = [x, y]
# print(dataset)

center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])

# Generate random data and center it to the three centers
data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3

dataset = np.concatenate((data_1, data_2, data_3), axis = 0)
mu, sigma = 0., 1. # mean and standard deviation
std_norm_samples = np.random.normal(mu, sigma, 1000)
std_norm_samples = np.reshape(std_norm_samples, (1000,1))

# plt.scatter(dataset[:,0], dataset[:,1], s=7)
# plt.show()

if __name__ == '__main__':
  unittest.main()
