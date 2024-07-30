import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D']
category1 = [3, 2, 5, 7]
category2 = [4, 5, 6, 3]
category3 = [7, 8, 3, 5]

plt.bar(labels, category1, label='Category 1')
plt.bar(labels, category2, bottom=category1, label='Category 2')
plt.bar(labels, category3, bottom=[i+j for i,j in zip(category1, category2)], label='Category 3')

plt.show()
