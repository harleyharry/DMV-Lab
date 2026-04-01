import numpy as np
import matplotlib.pyplot as plt

# Create clustered data with negative correlation
np.random.seed(0)

# Cluster 1
x1 = np.random.normal(2, 0.3, 30)
y1 = -x1 + np.random.normal(0, 0.2, 30)

# Cluster 2
x2 = np.random.normal(5, 0.3, 30)
y2 = -x2 + np.random.normal(0, 0.2, 30)

# Combine clusters
x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])

# Add outliers
x = np.append(x, [1, 6])
y = np.append(y, [3, -1])

# Plot scatter
plt.scatter(x, y, color='blue')

# Labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot with Clusters, Outliers, and Negative Correlation')

# Show plot
plt.show()