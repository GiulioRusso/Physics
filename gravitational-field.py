import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define grid
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Initial coordinates of the object (blue circle)
initial_x = 0
initial_y = 0

# Initial radius of the exclusion zone
initial_radius = 2

# Calculate initial distance
distance = np.sqrt((X - initial_x)**2 + (Y - initial_y)**2)

# Initial mask to remove points within the exclusion zone
mask = distance < initial_radius

# Calculate initial direction vectors
direction_x = -(X - initial_x) / distance
direction_y = -(Y - initial_y) / distance

# Calculate gravitational force
G = 6.67430  # Gravitational constant
mass = 1  # Mass of the object
force_magnitude = G * mass / distance**2
force_magnitude[mask] = 0  # Set force magnitude to zero where distance is within exclusion zone
force_x = force_magnitude * direction_x
force_y = force_magnitude * direction_y

# Create plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Plot initial vector field
quiver = ax.quiver(X, Y, force_x, force_y, scale=20)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gravitational Force Field')
plt.axis('square')
plt.grid(True)

# Draw initial blue circle at the origin
circle = plt.Circle((initial_x, initial_y), radius=1, color='blue', fill=True)
ax.add_patch(circle)

# Create sliders for object position
ax_x = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_y = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_x = Slider(ax_x, 'X Coordinate', -5.0, 5.0, valinit=initial_x)
slider_y = Slider(ax_y, 'Y Coordinate', -5.0, 5.0, valinit=initial_y)

# Function to update plot when sliders are moved
def update(val):
    # Update object coordinates
    x_coord = slider_x.val
    y_coord = slider_y.val
    
    # Update exclusion zone radius
    radius = 2
    
    # Update distance and direction vectors
    distance = np.sqrt((X - x_coord)**2 + (Y - y_coord)**2)
    mask = distance < radius
    direction_x = -(X - x_coord) / distance
    direction_y = -(Y - y_coord) / distance
    
    # Calculate gravitational force
    force_magnitude = G * mass / distance**2
    force_magnitude[mask] = 0
    force_x = force_magnitude * direction_x
    force_y = force_magnitude * direction_y
    
    # Update quiver plot
    quiver.set_UVC(force_x, force_y)
    
    # Update blue circle position
    circle.center = (x_coord, y_coord)
    
    # Redraw plot
    plt.draw()

# Attach update function to sliders
slider_x.on_changed(update)
slider_y.on_changed(update)

# Show plot
plt.show()
