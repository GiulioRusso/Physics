import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
mass = 10  # kg

# Function to calculate momentum
def calculate_momentum(velocity):
    return mass * velocity

# Function to update the plot when slider is moved
def update_momentum(val):
    ax.clear()
    velocity = slider_velocity.val
    momentum = calculate_momentum(velocity)
    
    # Draw rectangle
    ax.add_patch(plt.Rectangle((-2.5, -1), 5, 2, color='lightgray'))
    
    # Draw vector
    ax.arrow(0, 0, slider_velocity.val, 0, head_width=0.5, head_length=0.5, fc='r', ec='r')
    
    # Plot settings
    ax.annotate(f'Mass: {mass} kg\nVelocity: {velocity:.2f} m/s\nMomentum: {momentum:.2f} kg m/s', 
                xy=(0, 2), xytext=(0, mass), ha='center', fontsize=10, textcoords='offset points')
    ax.set_xlim(-10, 10)  # Adjust as needed
    ax.set_ylim(-5, 5)  # Adjust as needed
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(['Object', 'Velocity vector'])
    ax.set_title('Momentum visualization')
    plt.draw()

# Create initial plot
fig, ax = plt.subplots()

# Create slider
ax_velocity = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_velocity = Slider(ax_velocity, 'Velocity', 0, 10, valinit=0)

# Attach update function to slider
slider_velocity.on_changed(update_momentum)

# Initial update
update_momentum(None)

plt.show()
