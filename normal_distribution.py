import matplotlib.pyplot as plt
import numpy as np
import torch

mu, sigma = 0., 1. # mean and standard deviation
# s = np.random.normal(mu, sigma, 1000000)

# print(s.shape)
# print(s)

# # Verify the mean and the variance:


# # print(abs(mu - np.mean(s)) < 0.01)
# # # True



# # print(abs(sigma - np.std(s, ddof=1)) < 0.01)
# # # True

# # # Display the histogram of the samples, along with the probability density function:


# count, bins, ignored = plt.hist(s, 10000, density=True)
# print(count)
# print(bins)
# print(ignored)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                 np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#           linewidth=2, color='r')
# plt.show()
def get_samples(mu, sigma, sample_size):

  norm = torch.distributions.normal.Normal(mu, sigma)
  samples = norm.sample(sample_size)
  
  return samples



