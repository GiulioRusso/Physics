import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Arc

# Create the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

# Initial angle of incidence in degrees
angle_initial = 45  # degrees

# Function to update the plot with the new angles
def update(val):
    angle = slider_angle.val  # get the angle from the slider
    angle_rad = np.deg2rad(angle)  # convert to radians

    # Calculate the points for the incident ray
    # Starting at (x=-1) and calculating where it intersects y=0
    x_incident = np.array([-1, 0])  # x = 0 where it hits the ground
    y_incident = np.array([np.tan(np.pi/2 - angle_rad), 0])  # calculate y at x=-1 based on angle

    # Calculate the points for the reflected ray
    # Reflecting symmetrically off the ground
    x_reflected = np.array([0, 1])
    y_reflected = np.array([0, np.tan(np.pi/2 - angle_rad)])

    # Update the data for the incident and reflected rays
    line_incident.set_data(x_incident, y_incident)
    line_reflected.set_data(x_reflected, y_reflected)

    # Update the vertical line at the point of reflection
    reflection_line.set_data([0, 0], [-1, 1])  # Vertical line at x=0

    # Update the angles of incidence and reflection
    incident_angle_patch.theta2 = 90 + angle
    reflected_angle_patch.theta1 = 90 - angle

    # Redraw the figure
    fig.canvas.draw_idle()

# Initial setup for the incident and reflected rays
angle_rad_initial = np.deg2rad(angle_initial)
x_incident_initial = np.array([-1, 0])
y_incident_initial = np.array([np.tan(np.pi/2 - angle_rad_initial), 0])
x_reflected_initial = np.array([0, 1])
y_reflected_initial = np.array([0, np.tan(np.pi/2 - angle_rad_initial)])

# Plot the initial rays
line_incident, = ax.plot(x_incident_initial, y_incident_initial, label='Incident Ray')
line_reflected, = ax.plot(x_reflected_initial, y_reflected_initial, 'r--', label='Reflected Ray')

# Draw the vertical line at the point of reflection
reflection_line, = ax.plot([0, 0], [-1, 1], color='gray', linestyle='dashed', alpha=0.5)

# Set limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', 'box')
ax.legend()

# Draw the ground line
ax.axhline(0, color='gray', lw=2)

# Draw arcs to indicate angles
incident_angle_patch = Arc((0, 0), 0.4, 0.4, angle=0, theta1=90, theta2=90 + angle_initial, color='blue', label='Angle of Incidence')
reflected_angle_patch = Arc((0, 0), 0.4, 0.4, angle=0, theta1=90 - angle_initial, theta2=90, color='red', label='Angle of Reflection')
ax.add_patch(incident_angle_patch)
ax.add_patch(reflected_angle_patch)

# Create slider for controlling the angle of incidence
ax_angle = plt.axes([0.18, 0.1, 0.7, 0.03])
slider_angle = Slider(ax_angle, 'Incident\nAngle', 0, 90, valinit=angle_initial)

# Attach the update function to the slider
slider_angle.on_changed(update)

# Display the plot
plt.show()
