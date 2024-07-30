import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

plt.scatter(x, y)
plt.show()

sizes = [20, 50, 80, 200, 500]

plt.scatter(x, y, s=sizes)
plt.show()