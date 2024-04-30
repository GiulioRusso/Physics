import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate torque vector (cross product)
def calculate_torque(force, position):
    return np.cross(position, force)

# Function to update the plot when sliders are moved
def update_plot(val):
    ax.clear()
    
    # Fixed position vector (object at (5, 5, 5))
    position = np.array([5, 5, 5])
    
    # Get force vector from sliders
    force_x = slider_force_x.val
    force_y = slider_force_y.val
    force_z = slider_force_z.val
    force = np.array([force_x, force_y, force_z])
    
    # Calculate torque vector (cross product between position and force)
    torque = calculate_torque(force, position)
    
    # Draw position vector (from origin to object)
    ax.quiver(0, 0, 0, position[0], position[1], position[2], color='k', linestyle='--', label='Position Vector')
    
    # Draw object at the specified position
    ax.scatter(position[0], position[1], position[2], color='b', s=100, label='Object')
    
    # Draw force vector starting from the object
    ax.quiver(position[0], position[1], position[2], force[0], force[1], force[2], color='r', label='Force Vector')
    
    # Draw torque vector starting from the object
    ax.quiver(position[0], position[1], position[2], torque[0], torque[1], torque[2], color='g', label='Torque Vector')
    
    # Plot settings
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-10,10])
    ax.set_ylim([-10,10])
    ax.set_zlim([-10,10])
    ax.set_title('Torque Vector visualization')
    ax.legend()
    plt.draw()

# Create initial plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create sliders for force vector components
ax_force_x = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_force_y = plt.axes([0.1, 0.05, 0.65, 0.03])
ax_force_z = plt.axes([0.1, 0.15, 0.65, 0.03])
slider_force_x = Slider(ax_force_x, 'Force X', -10.0, 10.0, valinit=1)
slider_force_y = Slider(ax_force_y, 'Force Y', -10.0, 10.0, valinit=1)
slider_force_z = Slider(ax_force_z, 'Force Z', -10.0, 10.0, valinit=1)

# Attach update function to sliders
slider_force_x.on_changed(update_plot)
slider_force_y.on_changed(update_plot)
slider_force_z.on_changed(update_plot)

# Initial update
update_plot(None)

plt.show()
