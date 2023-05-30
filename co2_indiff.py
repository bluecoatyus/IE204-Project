import numpy as np
import matplotlib.pyplot as plt


# Define the utility function
def utility_function(x1, x2):
    return 5 * np.sqrt(x1) + 3 * x2


# Generate a range of values for x1 and x2
x1 = np.linspace(0.01, 10, 100)  # Avoid 0 for square root
x2 = np.linspace(0, 10, 100)

# Create a grid of values for x1 and x2
X1, X2 = np.meshgrid(x1, x2)

# Calculate the utility values for each combination of x1 and x2
Z = utility_function(X1, X2)

# Set the utility level for the indifference curves
utility_levels = [5, 10, 15, 20, 25, 30, 35]

# Plot the indifference curves
plt.figure()

# Plot the utility contours as dashed lines
contour = plt.contour(X1, X2, Z, utility_levels, cmap='viridis', linestyles='dashed')

# Plot circles at integer values on the utility levels
for level in utility_levels:
    # Find integer values that satisfy the utility function
    x1_int = np.arange(1, 10)
    x2_int = (level - 5 * np.sqrt(x1_int)) / 3

    # Exclude values of x2 below 0
    valid_indices = np.where(x2_int >= 0)
    x1_int = x1_int[valid_indices]
    x2_int = x2_int[valid_indices]

    # Plot circles at the valid integer values
    plt.scatter(x1_int, x2_int, marker='o', color='red')

# Set labels and title
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Indifference Curves for CO2 Emission')

# Add a colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Utility')

# Show the plot
plt.show()

