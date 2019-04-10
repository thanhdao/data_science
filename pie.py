import matplotlib.pyplot as plt

sizes = [20, 20, 45, 10]
labels = ['Cats', 'Dogs', 'Tigers', 'Goats']

plt.pie(sizes, labels=labels, autopct = "%.2f")

plt.axes().set_aspect('equal')
plt.show()