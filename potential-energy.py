import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
mass = 10  # kg
gravity = 9.81  # m/s^2

# Function to calculate potential energy
def calculate_potential_energy(height):
    return mass * gravity * height

# Function to update the plot when slider is moved
def update_potential_energy(val):
    ax.clear()
    height = slider_height.val
    potential_energy = calculate_potential_energy(height)
    ax.plot([0], [height], 'o', markersize=mass, color='b')  # Object represented by a circle
    ax.annotate(f'Mass: {mass} kg\nHeight: {height:.2f} m\nPotential Energy: {potential_energy:.2f} J', 
                xy=(0, height), xytext=(0, mass), ha='center', fontsize=10, textcoords='offset points')
    ax.plot([0, 0], [0, height], 'g--')  # Dashed green line from origin to object
    ax.set_xlim(-15, 15)  # Adjust as needed
    ax.set_ylim(-1, 11)  # Adjust as needed
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(['Object', 'Height'])
    ax.set_title('Potential energy visualization')
    plt.draw()

# Create initial plot
fig, ax = plt.subplots()

# Create slider
ax_height = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_height = Slider(ax_height, 'Height', 0, 7, valinit=0)

# Attach update function to slider
slider_height.on_changed(update_potential_energy)

# Initial update
update_potential_energy(None)

plt.show()
