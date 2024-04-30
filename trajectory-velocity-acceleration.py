import numpy as np
import matplotlib.pyplot as plt

# Define time range
t = np.linspace(0, 10, 100)

# Define trajectory function (example: quadratic)
def trajectory(t):
    return 0.5 * t**2 # Replace with your own trajectory equation

# Calculate trajectory
position = trajectory(t)

# Calculate velocity (first derivative of position)
velocity = np.gradient(position, t)

# Calculate acceleration (second derivative of position)
acceleration = np.gradient(velocity, t)

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

# Plot position
ax1.plot(t, position, label='Position')
ax1.set_ylabel('Position')
ax1.legend()

# Plot velocity
ax2.plot(t, velocity, label='Velocity', color='orange')
ax2.set_ylabel('Velocity')
ax2.legend()

# Plot acceleration
ax3.plot(t, acceleration, label='Acceleration', color='green')
ax3.set_ylabel('Acceleration')
ax3.set_xlabel('Time')
ax3.legend()

plt.tight_layout()
plt.show()
