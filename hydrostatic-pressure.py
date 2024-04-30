import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
rho = 1000  # Density of water (kg/m^3)

# Function to calculate hydrostatic pressure
def hydrostatic_pressure(depth):
    pressure = rho * g * depth
    return pressure

# Function to update plot
def update_plot(val):
    # Calculate hydrostatic pressure
    pressure = hydrostatic_pressure(slider_depth.val)
    
    # Clear previous plot
    ax.clear()
    
    # Plot water level
    ax.plot([0, 1], [0, 0], 'b-', linewidth=2)

    # Plot text
    ax.text(0.5, -slider_depth.val/2, f'Depth = {slider_depth.val:.2f} m', fontsize=12, ha='center')
    ax.text(0.5, 1, f'Pressure = {pressure:.2f} Pa', fontsize=12, ha='center')

    # Plot depth vector
    ax.quiver(0.5, 0, 0, -slider_depth.val, angles='xy', scale_units='xy', scale=1, color='r')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(-10, 2)
    ax.set_xlabel('Width (m)')
    ax.set_ylabel('Depth (m)')
    ax.set_title('Hydrostatic Pressure')
    ax.grid(True)

# Create initial plot
fig, ax = plt.subplots()

# Create slider
ax_depth = plt.axes([0.1, 0.01, 0.65, 0.03])
slider_depth = Slider(ax_depth, 'Depth', 0, 10, valinit=0)

# Attach update function to slider
slider_depth.on_changed(update_plot)

# Initial update
update_plot(None)

plt.show()
