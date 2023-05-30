import numpy as np
import matplotlib.pyplot as plt

# Define the utility function
def utility_function(x1, x2):
    return x1 * x2**1.5

# Define the utility level
utility_level = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Set desired utility levels

# Create a grid of integer values for x1 and x2
x1 = np.arange(1, 6)
x2 = np.arange(1, 6)

# Generate data for the plot
x1, x2 = np.meshgrid(x1, x2)     # Create a grid of x1 and x2 values
u = utility_function(x1, x2)      # Calculate the utility values

# Create the plot
fig, ax = plt.subplots()
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Indifference Curves')

# Plot the indifference curves
for level in utility_level:
    curve = ax.contour(x1, x2, u, levels=[level], colors='b', linestyles='dashed')
    x1_points = curve.allsegs[0][0][:, 0]
    x2_points = curve.allsegs[0][0][:, 1]
    ax.plot(x1_points, x2_points, 'ro', markersize=4)

# Show the plot
plt.show()

