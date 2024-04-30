import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Arc

# Create the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

# Refractive indices
n_air = 1.0
n_water = 1.333

# Initial angle of incidence in degrees
angle_initial = 45  # degrees

# Function to update the plot with the new angles
def update(val):
    angle_incidence = slider_angle.val  # get the angle from the slider
    angle_incidence_rad = np.deg2rad(angle_incidence)  # convert to radians

    # Calculate the angle of refraction using Snell's Law
    angle_refraction_rad = np.arcsin((n_air / n_water) * np.sin(angle_incidence_rad))

    # Calculate the points for the incident ray
    x_incident = np.array([-1, 0])  # x = 0 where it hits the water surface
    y_incident = np.array([np.tan(np.pi/2 - angle_incidence_rad), 0])  # calculate y at x=-1

    # Calculate the points for the refracted ray
    x_refracted = np.array([0, 1])
    y_refracted = np.array([0, np.tan(np.pi/2 - angle_refraction_rad)])

    # Update the data for the incident and refracted rays
    line_incident.set_data(x_incident, y_incident)
    line_refracted.set_data(x_refracted, y_refracted)

    # Update the vertical line at the point of reflection
    reflection_line.set_data([0, 0], [-1, 1])  # Vertical line at x=0

    # Update the angles of incidence and refraction
    incident_angle_patch.theta2 = 90 + angle_incidence
    refracted_angle_patch.theta1 = 90 - np.degrees(angle_refraction_rad)

    # Redraw the figure
    fig.canvas.draw_idle()

# Initial setup for the incident and refracted rays
angle_incidence_rad_initial = np.deg2rad(angle_initial)
angle_refraction_rad_initial = np.arcsin((n_air / n_water) * np.sin(angle_incidence_rad_initial))

x_incident_initial = np.array([-1, 0])
y_incident_initial = np.array([np.tan(np.pi/2 - angle_incidence_rad_initial), 0])
x_refracted_initial = np.array([0, 1])
y_refracted_initial = np.array([0, np.tan(np.pi/2 - angle_refraction_rad_initial)])

# Plot the initial rays
line_incident, = ax.plot(x_incident_initial, y_incident_initial, label='Incident Ray (Air: n1 = 1)')
line_refracted, = ax.plot(x_refracted_initial, y_refracted_initial, 'g--', label='Refracted Ray (Water: n2 = 1.333)')

# Draw the vertical line at the point of refraction
reflection_line, = ax.plot([0, 0], [-1, 1], color='gray', linestyle='dashed', alpha=0.5)

# Set limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', 'box')
ax.legend()

# Draw the ground line (interface between air and water)
ax.axhline(0, color='gray', lw=2)

# Draw water
ax.add_patch(plt.Rectangle((0, -1), 1.5, 2, color='lightblue'))

# Draw arcs to indicate angles
incident_angle_patch = Arc((0, 0), 0.4, 0.4, angle=0, theta1=90, theta2=90 + angle_initial, color='blue', label='Angle of Incidence')
refracted_angle_patch = Arc((0, 0), 0.4, 0.4, angle=0, theta1=90 - np.degrees(angle_refraction_rad_initial), theta2=90, color='green', label='Angle of Refraction')
ax.add_patch(incident_angle_patch)
ax.add_patch(refracted_angle_patch)

# Create slider for controlling the angle of incidence
ax_angle = plt.axes([0.18, 0.1, 0.7, 0.03])
slider_angle = Slider(ax_angle, 'Incidence\nAngle', 0, 90, valinit=angle_initial)

# Attach the update function to the slider
slider_angle.on_changed(update)

# Display the plot
plt.show()
