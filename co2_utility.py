import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the utility function
def utility_function(x1, x2):
    return 4*np.sqrt(x1) + 3*x2

# Generate a range of values for x1 and x2
x1 = np.linspace(0, 5, 100)
x2 = np.linspace(0, 5, 100)
X1, X2 = np.meshgrid(x1, x2)

# Calculate the utility values for each combination of x1 and x2
Z = utility_function(X1, X2)

# Create a 3D plot of the utility function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the utility surface
ax.plot_surface(X1, X2, Z, cmap='viridis')

# Set labels and title
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Utility')
ax.set_title('Utility Function: 4√(x1) + 3x2')

# Show the plot
plt.show()

