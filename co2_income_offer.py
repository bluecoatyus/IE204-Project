import matplotlib.pyplot as plt
import numpy as np

# Define the utility function
def utility(x1, x2):
    return 5 * np.sqrt(x1) + 3 * x2

# Define the income range
income_range = np.linspace(0, 700, 100)

# Calculate the corresponding demand for x2 at different income levels
demand_x2 = np.full_like(income_range, 1)  # Scale the income range to match the demand range [0, 5]

# Plot the Engel curve
plt.plot(demand_x2, income_range)

# Set labels and title
plt.xlabel('Demand(x1)')
plt.ylabel('Income(m) 100k scale')
plt.title('Income offer Curve')

# Show the plot
plt.show()
