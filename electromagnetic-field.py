import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data for a sinusoidal curve in 2D plane
t = np.linspace(0, 4*np.pi, 30)
x = np.sin(t)
y = t

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the existing sinusoidal curve in XY plane
ax.plot(x, y, np.zeros_like(x), color='g', label='Magnetic field')

# Add vectors along the curve
for i in range(len(t)):
    # Calculate vector length equal to sine value at each point
    vec_length = np.sin(y[i])
    
    # Draw vector at point (0, y_i, 0)
    ax.quiver(0, y[i], 0, vec_length, 0, 0, color='g', alpha=0.5, arrow_length_ratio=0.1)

# Plot the new sinusoidal curve in YZ plane
new_x = np.zeros_like(t)  # x-coordinates are all zeros for YZ plane
new_y = np.sin(x)  # y-coordinates for the YZ plane
ax.plot(new_x, y, new_y, color='r', label='Electrical field')

# Add vectors along the curve in YZ plane
for i in range(len(t)):
    vec_length = np.sin(x[i])
    ax.quiver(0, y[i], 0, 0, 0, vec_length, color='r', alpha=0.5, arrow_length_ratio=0.1)

# Add legend
ax.legend()

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Electromagnetic field')

# Show plot
plt.show()
