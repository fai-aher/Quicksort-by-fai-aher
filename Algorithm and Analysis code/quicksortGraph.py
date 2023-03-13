

import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 100000, 100000) # Input size from 1 to 100000
c = 1.39 * np.log2(n) # Complexity

plt.plot(n, c)
plt.title('Average Complexity of Quick Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Complexity')
plt.show()

