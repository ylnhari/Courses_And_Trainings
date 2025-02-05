"""
This module visualizes a scatter plot of sample data points and a decision boundary line that can be adjusted using sliders.
It also displays a table with example data.
Usage:
------
    1. Run the script to display the scatter plot and table.
    2. Use the sliders below the scatter plot to adjust the slope and intercept of the decision boundary line.
    3. Observe how the decision boundary line changes in real-time as you adjust the sliders.

Dependencies:
-------------
    - matplotlib
    - numpy

Functions:
----------
    - update(val): Updates the decision boundary line based on the current values of the slope and intercept sliders.

Example:
--------
# To run the script, simply execute it in a Python environment:
    python ml_visualize.py

Notes:
------
    - The sample data is generated randomly for demonstration purposes. Replace it with your actual data as needed.
    - The table on the right side of the plot displays example data. Replace it with your actual data as needed.

"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.table import Table
from matplotlib.font_manager import FontProperties 
# Generate some sample data (replace with your actual data)
np.random.seed(0)
n_samples = 200
X = np.r_[np.random.randn(n_samples, 2) - [2, 2], np.random.randn(n_samples, 2) + [2, 2]]
y = [0] * n_samples + [1] * n_samples  # 0 and 1 represent two classes

# Set up the figure and axes (adjust figsize for better layout)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns
plt.subplots_adjust(bottom=0.25, left=0.1, wspace=0.3)  # Adjust spacing

# Scatter plot (on the left axes)
scatter_ax = ax[0]  # Assign the first axes to scatter_ax
colors = ['green' if label == 0 else 'orange' for label in y]
scatter = scatter_ax.scatter(X[:, 0], X[:, 1], c=colors, edgecolors='k')

# Initial decision boundary (a line)
x_line = np.linspace(X[:, 0].min() - 2, X[:, 0].max() + 2, 100)
initial_slope = 0.5
initial_intercept = 4.16
line, = scatter_ax.plot(x_line, initial_slope * x_line + initial_intercept, color='red', label="Decision Boundary")

# Create the slider axes
ax_slope = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_intercept = fig.add_axes([0.25, 0.05, 0.65, 0.03])

# Create the sliders
slope_slider = Slider(ax_slope, 'Slope', -2.0, 2.0, valinit=initial_slope)
intercept_slider = Slider(ax_intercept, 'Intercept', -5, 5, valinit=initial_intercept)

# Update function for the slider
def update(val):
    """
    Update the line plot based on the current values of the slope and intercept sliders.

    Parameters:
    val : float
        The value from the slider (not used in the function but required by the slider event).

    Returns:
    None

    This function updates the y-data of the line plot using the current values of the slope and intercept sliders,
    and then redraws the plot.

    Usage example:
    --------------
    # Assuming you have a matplotlib figure, axis, line, and sliders set up:
    slope_slider.on_changed(update)
    intercept_slider.on_changed(update)
    """
    slope = slope_slider.val
    intercept = intercept_slider.val
    line.set_ydata(slope * x_line + intercept)  # Update the line data
    fig.canvas.draw_idle()  # Redraw the plot

# Connect the slider to the update function
slope_slider.on_changed(update)
intercept_slider.on_changed(update)

# Meaningful Feature Names and Context
scatter_ax.set_xlabel('Feature 1: Willingness to Help Others (Score)')
scatter_ax.set_ylabel('Feature 2: Level of Social Interaction (Score)')
scatter_ax.set_title('Categorizing People Based on Personality Traits')
scatter_ax.legend()
scatter_ax.grid(True)

# Example Data for the Table (replace with your actual data)
table_data = [
    ["Person 1", X[250, 0].round(1), X[250, 1].round(1), "Introvert" if y[250] == 0 else "Extrovert"],
    ["Person 2", X[10, 0].round(1), X[10, 1].round(1), "Extrovert" if y[10] == 1 else "Introvert"],
    ["Person 3", X[350, 0].round(1), X[350, 1].round(1), "Introvert" if y[350] == 0 else "Extrovert"],
    ["Person 4", X[100, 0].round(1), X[100, 1].round(1), "Extrovert" if y[100] == 1 else "Introvert"],

]


# Create the table (on the right axes)
table_ax = ax[1]
table = Table(table_ax, bbox=[0, 0, 1, 1])

# More options (size, family, weight)
#font_prop = FontProperties(size=134, family='serif', weight='bold')
for i, row in enumerate(table_data):
    for j, cell in enumerate(row):
        table.add_cell(i, j, width=0.2, height=0.1, text=cell, loc='center')#, fontproperties=font_prop)

table_ax.add_table(table)
table_ax.axis('off')  # Hide the table axes


plt.show()
