import matplotlib.pyplot as plt


years = [1983, 1984, 1985, 1986, 1987]
total_populations = [8939007, 8954518, 8960387, 8956741, 8943721]

plt.plot(years, total_populations)

plt.title("Year vs Population in Bulgaris")
plt.xlabel("Year")
plt.ylabel("Total Population")
# plt.xticks([1,2,3,4,5])
# plt.yticks()
plt.show()
