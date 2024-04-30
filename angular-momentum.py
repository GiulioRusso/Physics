import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate the angular momentum vector
def calculate_angular_momentum(inertia, length):
    return np.array([0, 0, inertia * length])

# Function to update the plot when sliders are moved
def update_plot(val):
    ax.clear()
    
    # Parameters
    theta = np.linspace(0, 2 * np.pi, 100)  # Angle range for circle
    
    # Circular trajectory
    x_circle = 5*np.cos(theta)
    y_circle = 5*np.sin(theta)
    z_circle = np.zeros_like(theta)
    ax.plot(x_circle, y_circle, z_circle, color='gray', label='Circular Trajectory')
    
    # Sphere object at a specific point on the circle
    object_point = (np.cos(position) * np.cos(position), np.sin(position) * np.cos(position), np.sin(position))
    ax.scatter(5*object_point[0], 5*object_point[1], 5*object_point[2], color='blue', s=100, label='Object')
    
    # Calculate angular momentum vector
    angular_momentum = calculate_angular_momentum(slider_inertia.val, slider_angular_velocity.val)
    
    # Draw angular velocity vector at the center of the circle
    ax.quiver(0, 0, 0, 0, 0, slider_angular_velocity.val, color='k', label='Angular Velocity')

    # Draw angular momentum vector at the center of the circle
    ax.quiver(0, 0, 0, angular_momentum[0], angular_momentum[1], angular_momentum[2], color='r', label='Angular Momentum')
    
    # Plot settings
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-10,10])
    ax.set_ylim([-10,10])
    ax.set_zlim([-10,10])
    ax.set_title('Angular Momentum visualization')
    ax.legend()
    plt.draw()

# Create initial plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create sliders for inertia and angular velocity
ax_inertia = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_angular_velocity = plt.axes([0.1, 0.05, 0.65, 0.03])
slider_inertia = Slider(ax_inertia, 'Inertia', 0.1, 10.0, valinit=1.0)
slider_angular_velocity = Slider(ax_angular_velocity, 'Angular Velocity', 0.1, 10.0, valinit=1.0)

# Attach update function to sliders
slider_inertia.on_changed(update_plot)
slider_angular_velocity.on_changed(update_plot)

# Initial parameters
position = 0.0  # Initial position on the circle

# Initial update
update_plot(None)

plt.show()
