import numpy as np
import matplotlib.pyplot as plt

# Define the utility function
def utility_function(x1, x2):
    return x1 * x2**1.5

# Generate data for the plot
x1 = np.linspace(0.1, 10, 100)  # Range of x1 values
x2 = np.linspace(0.1, 10, 100)  # Range of x2 values
x1, x2 = np.meshgrid(x1, x2)    # Create a grid of x1 and x2 values
u = utility_function(x1, x2)     # Calculate the utility values

# Create the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(x1, x2, u, cmap='viridis')

# Set the labels and title
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Utility')
ax.set_title('Utility Function: U(x1, x2) = x1 * x2^1.5')

# Show the plot
plt.show()
