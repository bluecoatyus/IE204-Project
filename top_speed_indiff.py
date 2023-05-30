import numpy as np
import matplotlib.pyplot as plt

# Define the utility function
def utility_function(x1, x2):
    return x1 + x2

# Define the utility levels
utility_levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Set desired utility levels

# Generate data for the plot
x = np.linspace(0, 5, 100)  # Range of x values
x1, x2 = np.meshgrid(x, x)  # Create a grid of x1 and x2 values
u = utility_function(x1, x2)  # Calculate the utility values

# Create the plot
fig, ax = plt.subplots()
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Indifference Curves')

# Plot the indifference curves
for level in utility_levels:
    contour = ax.contour(x1, x2, u, levels=[level], colors='b', linestyles='dashed')

    # Extract the x1 and x2 points from the contour line
    x1_points = contour.collections[0].get_paths()[0].vertices[:, 0]
    x2_points = contour.collections[0].get_paths()[0].vertices[:, 1]

    # Round the x1 and x2 values to the nearest integer
    x1_int = np.round(x1_points)
    x2_int = np.round(x2_points)

    # Plot circles at the valid integer values
    plt.scatter(x1_int, x2_int, marker='o', color='red')

# Show the plot
plt.show()
