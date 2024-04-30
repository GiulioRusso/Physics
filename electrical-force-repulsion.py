import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Rectangle
import numpy as np

# Charge parameters
q1 = 10  # Charge of Charge 1
q2 = 10  # Charge of Charge 2

# Charge positions
pos1 = np.array([0, 5])  # Position of Charge 1
pos2 = np.array([5, 5])  # Position of Charge 2

# Function to update the plot when sliders are moved
def update(val):

    # Calculate distance between Charges and unit direction vectors
    distance_vector = slider_x.val
    distance = np.linalg.norm(distance_vector)

    # Calculate gravitational forces
    k = 8.9875e-1  # Coulomb constant with e-1 instead e8 for visualization purpose
    force_magnitude1 = k * (abs(q1) * abs(q2)) / distance**2
    force_magnitude2 = -force_magnitude1

    ax.clear()
    # Plot Charge 1
    ax.scatter(pos1[0], pos1[1], s=abs(q1)*20, color='blue', label='Charge 1 = {}C'.format(q1))
    # Add plus sign for Charge 1
    ax.text(pos1[0], pos1[1], '+', fontsize=12, color='white', ha='center', va='center')
    # Plot Charge 2
    ax.scatter(slider_x.val, pos2[1], s=abs(q2)*20, color='blue', label='Charge 2 = {}C'.format(q2))
    # Add minus sign for Charge 2
    ax.text(slider_x.val, pos2[1], '+', fontsize=12, color='white', ha='center', va='center')
    # Plot force on Charge 1
    ax.quiver(pos1[0], pos1[1], -force_magnitude1, 0, angles='xy', scale_units='xy', scale=1, color='b', label='Electrical Force 1')
    # Plot force on Charge 
    ax.quiver(slider_x.val, pos2[1], -force_magnitude2, 0, angles='xy', scale_units='xy', scale=1, color='b', label='Electrical Force 2')
    ax.legend()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-1, 10)
    ax.set_title('Electrical Force visualization (repulsion)')
    plt.draw()

# Create initial plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Create sliders
ax_x = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_x = Slider(ax_x, 'X', 0.1, 10.0, valinit=5)

# Attach update function to sliders
slider_x.on_changed(update)

# Initial plot
update(None)

plt.show()
