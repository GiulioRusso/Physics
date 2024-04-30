import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
radius = 1  # Radius of the circle
circle_color = 'lightgray'  # Color of the circle
sphere_color = 'b'  # Color of the sphere
sphere_radius = 0.05  # Radius of the sphere

# Global variable to store previous slider value
prev_position = 0

# Function to update the plot when slider is moved
def update_position(val):
    global prev_position  # Declare prev_position as global
    
    ax.clear()
    position = slider_position.val
    theta = position * 2 * np.pi  # Convert position to angle (radians)
    
    # Draw circle
    circle = plt.Circle((0, 0), radius, color=circle_color, fill=False)
    ax.add_artist(circle)
    
    # Draw sphere (circle representing the object)
    sphere_x = radius * np.cos(theta)
    sphere_y = radius * np.sin(theta)
    ax.plot(sphere_x, sphere_y, 'o', markersize=sphere_radius * 100, color=sphere_color)
    
    # Draw vector from object to center of the circle
    ax.arrow(sphere_x, sphere_y, -sphere_x/2, -sphere_y/2, head_width=0.05, head_length=0.1, fc='r', ec='r', label="Centripetal Force")
    
    # Determine direction of green vector based on change in slider value
    direction = np.sign(position - prev_position)
    prev_position = position

    if direction > 0:
        # Calculate tangent vector (counter clockwise)
        tangent_angle = np.arctan2(sphere_x, -sphere_y)  # Angle of tangent vector
        tangent_x = np.cos(tangent_angle)
        tangent_y = np.sin(tangent_angle)
        # Draw angular velocity (going out of the plane)
        ax.scatter(0, 0, color='k', s=100, label='Angular velocity')
    else:
        # Calculate tangent vector (clockwise)
        tangent_angle = np.arctan2(-sphere_x, sphere_y)  # Angle of tangent vector
        tangent_x = np.cos(tangent_angle)
        tangent_y = np.sin(tangent_angle)
        # Draw angular velocity (going into the plane)
        ax.plot([0.1, -0.1], [0.1, -0.1], color='k', linestyle='-', label='Angular velocity')
        ax.plot([0.1, -0.1], [-0.1, 0.1], color='k', linestyle='-')
    
    # Draw tangent vector
    ax.arrow(sphere_x, sphere_y, tangent_x, tangent_y, head_width=0.05, head_length=0.1, fc='g', ec='g', label="Tangent velocity")
    
    # Plot settings
    ax.set_xlim(-1.5, 1.5)  # Adjust as needed
    ax.set_ylim(-1.5, 1.5)  # Adjust as needed
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.set_title('Circular motion')
    plt.draw()

# Create initial plot
fig, ax = plt.subplots()

# Create slider
ax_position = plt.axes([0.2, 0, 0.65, 0.03])
slider_position = Slider(ax_position, 'Position', 0, 1, valinit=0)

# Attach update function to slider
slider_position.on_changed(update_position)

# Initial update
update_position(None)

plt.show()
