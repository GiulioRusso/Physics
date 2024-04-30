import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
rho_water = 1000  # Density of water (kg/m^3)

# Function to calculate buoyant force
def buoyant_force(width, height):
    volume_submerged = width * height
    buoyant_force = rho_water * g * volume_submerged
    return buoyant_force

# Function to update plot
def update_plot(depth):
    # Clear previous plot
    ax.clear()
    
    # Calculate buoyant force
    if depth < 2:
        buoyant_force_value = buoyant_force(0.2, slider_depth.val)
    else:
        buoyant_force_value = buoyant_force(0.2, 2)
    
    # Plot water level
    ax.plot([0, 1], [0, 0], 'b-', linewidth=2)
    
    # Draw object
    ax.add_patch(plt.Rectangle((0.4, 0-depth), 0.2, 2, color='lightgray'))

    # Draw object area under the water
    if depth < 2:
        ax.add_patch(plt.Rectangle((0.4, 0-depth), 0.2, depth, color='blue', alpha=0.5))
    else:
        ax.add_patch(plt.Rectangle((0.4, 0-depth), 0.2, 2, color='blue', alpha=0.5))

    # Draw buoyant force (rescaled of 0.5*1e-3 for visualization purpose)
    ax.quiver(0.5, -slider_depth.val+2, 0, buoyant_force_value*0.5*1e-3, angles='xy', scale_units='xy', scale=1, color='g')
    
    # Update text
    ax.text(0.5, -depth/2, f'Depth = {depth:.2f} m', fontsize=12, ha='center')
    ax.text(0.5, 2, f'Buoyant Force = {buoyant_force_value:.2f} N', fontsize=12, ha='center')
    
    # Set limits and labels
    ax.set_xlim(0, 1)
    ax.set_ylim(-3, 3)
    ax.set_xlabel('Width (m)')
    ax.set_ylabel('Depth (m)')
    ax.set_title('Archimede principle')
    ax.grid(True)

# Create initial plot
fig, ax = plt.subplots()

# Create slider
ax_depth = plt.axes([0.1, 0.05, 0.65, 0.03])
slider_depth = Slider(ax_depth, 'Depth', 0, 3, valinit=0)

# Attach update function to slider
slider_depth.on_changed(update_plot)

# Initial update
update_plot(0)

plt.show()
