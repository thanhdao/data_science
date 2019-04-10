# scatter.py
import matplotlib.pyplot as plt

temp = [30, 32, 33, 28.5, 35, 29, 29]
ice_creams_count = [100, 115, 115, 75, 125, 79, 89]

plt.scatter(temp, ice_creams_count)

plt.title('Temperature vs Slid ice creams')
plt.xlabel('Temperature')
plt.ylabel('Sold ice creams count')
plt.show()