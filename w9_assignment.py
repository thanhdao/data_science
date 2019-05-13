import matplotlib.pyplot as plt
import pandas as pd

from random import *
import numpy as np
import seaborn as sns
import scipy.stats

# W9_assignment

# Load the dataset: https://python-graph-gallery.com/wp-content/uploads/mtcars.csv'
data_frame = pd.read_csv('mtcars.csv')
# print(data_frame)

# 1.     Compute the correlation matrix
corr = data_frame.corr()
print(corr)

# 2.     Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 3.     Draw the heatmap with the mask
sns.set(style="white")
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()

# Biased coin ? 60 heads have been found over 100 flips, is it coins biased ?

# 1. Model the data: number of heads follow a Binomial disctribution.
N, P = 100, 0.6

# 2. Compute model parameters: N=100, P=60/100

# 3. Compute a test statistic, same as frequency.
S = np.random.binomial(N, P, 1000)
# print(S)
# 4. Compute a test statistic: 60/100.
#tobs = 2.39687663116 # assume the t-value
succes = np.linspace(30, 70, 41)
plt.plot(succes, scipy.stats.binom.pmf(succes, 100, 0.5), 'b-', label="Binomial(100, 0.5)")
upper_succes_tvalues = succes[succes > 60]
plt.fill_between(upper_succes_tvalues, 0, scipy.stats.binom.pmf(upper_succes_tvalues, 100, 0.5), alpha=.8, label="p-value")
_ = plt.legend()
pval = 1 - scipy.stats.binom.cdf(60, 100, 0.5)
print(pval)
plt.show()