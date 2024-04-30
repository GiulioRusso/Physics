import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define grid
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Initial coordinates of the positive charge (blue circle)
initial_x_pos = 0
initial_y_pos = 0

# Initial coordinates of the negative charge (red circle)
initial_x_neg = 3
initial_y_neg = -3

# Initial radius of the exclusion zone
initial_radius = 2

# Calculate initial distance for the positive charge
distance_pos = np.sqrt((X - initial_x_pos)**2 + (Y - initial_y_pos)**2)

# Initial mask to remove points within the exclusion zone for the positive charge
mask_pos = distance_pos < initial_radius

# Calculate initial distance for the negative charge
distance_neg = np.sqrt((X - initial_x_neg)**2 + (Y - initial_y_neg)**2)

# Initial mask to remove points within the exclusion zone for the negative charge
mask_neg = distance_neg < initial_radius

# Calculate initial direction vectors for the positive charge
direction_x_pos = (X - initial_x_pos) / distance_pos
direction_y_pos = (Y - initial_y_pos) / distance_pos

# Calculate initial direction vectors for the negative charge
direction_x_neg = (X - initial_x_neg) / distance_neg
direction_y_neg = (Y - initial_y_neg) / distance_neg

# Calculate Electrical force for the positive charge
k = 6.67430  # Coulomb constant
charge_pos = 1  # Charge of the positive object
force_magnitude_pos = k * charge_pos / distance_pos**2
force_magnitude_pos[mask_pos | mask_neg] = 0  # Set force magnitude to zero where distance is within exclusion zone
force_x_pos = force_magnitude_pos * direction_x_pos
force_y_pos = force_magnitude_pos * direction_y_pos

# Calculate Electrical force for the negative charge
charge_neg = -1  # Charge of the negative object
force_magnitude_neg = k * charge_neg / distance_neg**2
force_magnitude_neg[mask_neg | mask_pos] = 0  # Set force magnitude to zero where distance is within exclusion zone
force_x_neg = force_magnitude_neg * direction_x_neg
force_y_neg = force_magnitude_neg * direction_y_neg

# Calculate total force vector (sum of force vectors due to both charges)
force_x_total = force_x_pos + force_x_neg
force_y_total = force_y_pos + force_y_neg

# Create plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.4)

ax.set_aspect('equal')
ax.set_title("Electrical field visualization")

# Plot total force vector
quiver = ax.quiver(X, Y, force_x_total, force_y_total, scale=20, color='purple', label='Total Force')

# Draw initial blue circle at the origin for the positive charge
circle_pos = plt.Circle((initial_x_pos, initial_y_pos), radius=1, color='blue', fill=True)
ax.add_patch(circle_pos)

# Draw initial red circle at the origin for the negative charge
circle_neg = plt.Circle((initial_x_neg, initial_y_neg), radius=1, color='red', fill=True)
ax.add_patch(circle_neg)

# Initial position of the plus sign for the positive charge
plus_sign_pos = ax.text(initial_x_pos, initial_y_pos, '+', fontsize=12, color='white', ha='center', va='center')

# Initial position of the minus sign for the negative charge
minus_sign_neg = ax.text(initial_x_neg, initial_y_neg, '-', fontsize=12, color='white', ha='center', va='center')

# Create sliders for object positions
ax_x_pos = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_y_pos = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_x_pos = Slider(ax_x_pos, 'X Coordinate (Positive)', -5.0, 5.0, valinit=initial_x_pos)
slider_y_pos = Slider(ax_y_pos, 'Y Coordinate (Positive)', -5.0, 5.0, valinit=initial_y_pos)

ax_x_neg = plt.axes([0.25, 0.25, 0.65, 0.03])
ax_y_neg = plt.axes([0.25, 0.2, 0.65, 0.03])
slider_x_neg = Slider(ax_x_neg, 'X Coordinate (Negative)', -5.0, 5.0, valinit=initial_x_neg)
slider_y_neg = Slider(ax_y_neg, 'Y Coordinate (Negative)', -5.0, 5.0, valinit=initial_y_neg)

# Function to update plot when sliders are moved
def update(val):
    # Update positive charge coordinates
    x_coord_pos = slider_x_pos.val
    y_coord_pos = slider_y_pos.val
    
    # Update negative charge coordinates
    x_coord_neg = slider_x_neg.val
    y_coord_neg = slider_y_neg.val
    
    # Update exclusion zone radius
    radius = 2
    
    # Update distance and direction vectors for the positive charge
    distance_pos = np.sqrt((X - x_coord_pos)**2 + (Y - y_coord_pos)**2)
    mask_pos = distance_pos < radius
    direction_x_pos = (X - x_coord_pos) / distance_pos
    direction_y_pos = (Y - y_coord_pos) / distance_pos
    
    # Update distance and direction vectors for the negative charge
    distance_neg = np.sqrt((X - x_coord_neg)**2 + (Y - y_coord_neg)**2)
    mask_neg = distance_neg < radius
    direction_x_neg = (X - x_coord_neg) / distance_neg
    direction_y_neg = (Y - y_coord_neg) / distance_neg
    
    # Calculate Electrical force for the positive charge
    force_magnitude_pos = k * charge_pos / distance_pos**2
    force_magnitude_pos[mask_pos | mask_neg] = 0
    force_x_pos = force_magnitude_pos * direction_x_pos
    force_y_pos = force_magnitude_pos * direction_y_pos
    
    # Calculate Electrical force for the negative charge
    force_magnitude_neg = k * charge_neg / distance_neg**2
    force_magnitude_neg[mask_neg | mask_pos] = 0
    force_x_neg = force_magnitude_neg * direction_x_neg
    force_y_neg = force_magnitude_neg * direction_y_neg

    # Calculate total force vector (sum of force vectors due to both charges)
    force_x_total = force_x_pos + force_x_neg
    force_y_total = force_y_pos + force_y_neg

    # Update quiver plot
    quiver.set_UVC(force_x_total, force_y_total)
    
    # Update blue circle position for the positive charge
    circle_pos.center = (x_coord_pos, y_coord_pos)

    # Update red circle position for the negative charge
    circle_neg.center = (x_coord_neg, y_coord_neg)
    
    # Update plus sign position for the positive charge
    plus_sign_pos.set_position((x_coord_pos, y_coord_pos))

    # Update minus sign position for the negative charge
    minus_sign_neg.set_position((x_coord_neg, y_coord_neg))
    
    # Redraw plot
    plt.draw()

# Attach update function to sliders for the positive charge
slider_x_pos.on_changed(update)
slider_y_pos.on_changed(update)

# Attach update function to sliders for the negative charge
slider_x_neg.on_changed(update)
slider_y_neg.on_changed(update)

# Show plot
plt.show()
