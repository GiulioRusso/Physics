import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Define grid
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
z = np.linspace(-5, 5, 10)
X, Y, Z = np.meshgrid(x, y, z)

# Initial values for velocity vector origin
initial_origin_x = 0
initial_origin_y = 0
initial_origin_z = 0

# Initial value for velocity magnitude
initial_magnitude = 1

# Define magnetic field vector components
magnetic_field_x = 1
magnetic_field_y = 0
magnetic_field_z = 0

# Plot magnetic field vector in every point of the space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
quiver_velocity = None  # Initialize quiver_velocity as None
quiver_magnetic_field = ax.quiver(X, Y, Z, magnetic_field_x, magnetic_field_y, magnetic_field_z, color='green', length=0.5, alpha=0.5, label="Magnetic field")
quiver_lorentz = None

# Initial end point of velocity vector
end_point_x = initial_origin_x + initial_magnitude
end_point_y = initial_origin_y
end_point_z = initial_origin_z

# Define function to update plot when sliders are moved
def update(val):
    global quiver_velocity, quiver_lorentz  # Declare quiver_velocity and quiver_lorentz as global variables
    
    # Get current slider values
    end_point_x = slider_end_point_x.val
    end_point_y = slider_end_point_y.val
    end_point_z = slider_end_point_z.val
    
    # Update quiver plot with new end point of velocity vector
    if quiver_velocity:
        quiver_velocity.remove()  # Remove the previous quiver plot if it exists
    quiver_velocity = ax.quiver(initial_origin_x, initial_origin_y, initial_origin_z, 
                                 end_point_x - initial_origin_x, end_point_y - initial_origin_y, end_point_z - initial_origin_z,
                                 color='blue', label="Velocity")
    
    # Calculate Lorentz force vector
    charge = 1  # Assuming positive charge
    lorentz_force_x = charge * (end_point_y * magnetic_field_z - end_point_z * magnetic_field_y)
    lorentz_force_y = charge * (end_point_z * magnetic_field_x - end_point_x * magnetic_field_z)
    lorentz_force_z = charge * (end_point_x * magnetic_field_y - end_point_y * magnetic_field_x)
    
    # Update quiver plot with Lorentz force vector
    if quiver_lorentz:
        quiver_lorentz.remove()  # Remove the previous quiver plot if it exists
    quiver_lorentz = ax.quiver(initial_origin_x, initial_origin_y, initial_origin_z, 
                                lorentz_force_x, lorentz_force_y, lorentz_force_z,
                                color='red', label="Lorentz Force")
    
    # Redraw plot
    fig.canvas.draw_idle()
    ax.legend()

# Add sliders for end point of velocity vector
ax_end_point_x = plt.axes([0.25, 0.05, 0.65, 0.03])
ax_end_point_y = plt.axes([0.25, 0.02, 0.65, 0.03])
ax_end_point_z = plt.axes([0.25, 0.08, 0.65, 0.03])
slider_end_point_x = Slider(ax_end_point_x, 'End Point X', -5.0, 5.0, valinit=end_point_x)
slider_end_point_y = Slider(ax_end_point_y, 'End Point Y', -5.0, 5.0, valinit=end_point_y)
slider_end_point_z = Slider(ax_end_point_z, 'End Point Z', -5.0, 5.0, valinit=end_point_z)

# Attach update function to sliders
slider_end_point_x.on_changed(update)
slider_end_point_y.on_changed(update)
slider_end_point_z.on_changed(update)

# Set equal aspect ratio for all axes
ax.set_box_aspect([1, 1, 1])
ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_zlim([-5,5])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Magnetic Force visualization")
ax.legend()

# Show plot
plt.show()
