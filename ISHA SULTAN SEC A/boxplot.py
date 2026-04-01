import matplotlib.pyplot as plt

# Dataset
weights = [25, 28, 29, 29, 30, 34, 35, 35, 37, 38]

# Draw boxplot
plt.boxplot(weights)

# Add labels and title
plt.xlabel('Data')
plt.ylabel('Weights (grams)')
plt.title('Box Plot of Box Weights')

# Display the plot
plt.show()