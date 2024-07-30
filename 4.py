import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)

plt.hist(data)
plt.show()

data = np.random.randn(100)
plt.boxplot(data)
plt.show()
