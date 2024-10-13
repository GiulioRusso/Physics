import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Rectangle
import numpy as np

# Object parameters
mass1 = 10  # Mass of object 1
mass2 = 5   # Mass of object 2

# Object positions
pos1 = np.array([0, 5])  # Position of object 1
pos2 = np.array([5, 5])  # Position of object 2

# Function to update the plot when sliders are moved
def update(val):

    # Calculate distance between objects and unit direction vectors
    distance_vector = slider_x.val
    distance = np.linalg.norm(distance_vector)

    # Calculate gravitational forces
    G = 6.67430e-1  # Gravitational constant with e-1 instead e-11 for visualization purpose
    force_magnitude1 = G * (mass1 * mass2) / distance**2
    force_magnitude2 = -force_magnitude1

    ax.clear()
    # Plot object 1
    ax.scatter(pos1[0], pos1[1], s=mass1*20, color='blue', label='Object 1 (Mass {})'.format(mass1))
    # Plot object 2
    ax.scatter(slider_x.val, pos2[1], s=mass2*20, color='red', label='Object 2 (Mass {})'.format(mass2))
    # Plot force on object 1
    ax.quiver(pos1[0], pos1[1], force_magnitude1, 0, angles='xy', scale_units='xy', scale=1, color='b', label='Gravitational Force 1')
    # Plot force on object 
    ax.quiver(slider_x.val, pos2[1], force_magnitude2, 0, angles='xy', scale_units='xy', scale=1, color='r', label='Gravitational Force 2')
    ax.legend()
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_title('Gravitational Force visualization')
    plt.draw()

# Create initial plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Create sliders
ax_x = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_x = Slider(ax_x, 'X', 0.1, 10.0, valinit=0)

# Attach update function to sliders
slider_x.on_changed(update)

# Initial plot
update(None)

plt.show()
