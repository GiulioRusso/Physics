import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from matplotlib.patches import Arc

# Function to calculate work
def calculate_work(displacement_magnitude, force_magnitude, angle_deg):
    angle_rad = np.deg2rad(angle_deg)
    return displacement_magnitude * force_magnitude * np.cos(angle_rad)

# Function to update the plot when slider is moved
def update_work(val):
    ax.clear()
    
    # Draw displacement vector (fixed horizontal vector)
    ax.arrow(0, 0, displacement_magnitude, 0, head_width=0.5, head_length=0.5, fc='b', ec='b', label='Displacement Vector')
    
    # Calculate work
    force_magnitude = slider_force.val
    angle_deg = slider_angle.val
    work = calculate_work(displacement_magnitude, force_magnitude, angle_deg)
    
    # Calculate components of force vector
    force_x = force_magnitude * np.cos(np.deg2rad(angle_deg))
    force_y = force_magnitude * np.sin(np.deg2rad(angle_deg))

    # Draw rectangle
    ax.add_patch(plt.Rectangle((-2.5, -1), 5, 2, color='lightgray'))
    
    # Draw force vector
    ax.arrow(0, 0, force_x, force_y, head_width=0.5, head_length=0.5, fc='r', ec='r', label='Force Vector')

    # Draw the angle arc
    arc = Arc((0, 0), 2, 2, angle=0, theta1=0, theta2=angle_deg, color='darkviolet', linewidth=1.5)
    ax.add_patch(arc)
    
    # Plot settings
    ax.set_xlim(-10, 10)  # Adjust as needed
    ax.set_ylim(-5, 5)  # Adjust as needed
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Work: {work:.2f} J')
    ax.legend()
    plt.draw()

# Create initial plot
fig, ax = plt.subplots()

# Initial values
displacement_magnitude = 5  # Magnitude of the displacement vector

# Create sliders
ax_force = plt.axes([0.1, 0.05, 0.65, 0.03])
ax_angle = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_force = Slider(ax_force, 'Force', 0, 10, valinit=0)
slider_angle = Slider(ax_angle, 'Angle', 0, 360, valinit=0)

# Attach update function to sliders
slider_force.on_changed(update_work)
slider_angle.on_changed(update_work)

# Initial update
update_work(None)

plt.show()
