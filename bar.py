import matplotlib.pyplot as plt

labels = ['JavaScript', 'Java', 'Python', 'C#']
usage = [69.8, 45.3, 38.8, 34.3]

y_positions = range(len(labels))

plt.bar(y_positions, usage)
plt.xticks(y_positions, labels)
plt.ylabel('Usage (%)')
plt.title('Programming language usage')
plt.show()