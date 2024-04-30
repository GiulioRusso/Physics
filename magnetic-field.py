import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space
I = 1  # Current in the wire in Amperes
radius = 1  # Radius of the wire loop

# Define the circle representing the wire in 3D
theta = np.linspace(0, 2*np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(theta)  # Wire is in the x-y plane

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the wire
ax.plot(x, y, z, label='Wire with counter clockwise current', color='b')

# Grid of points in space where we want to calculate the magnetic field
X, Y, Z = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10), np.linspace(-1, 1, 5))

# Calculate the magnetic field using the Biot-Savart Law simplified for symmetry
Bx = np.zeros_like(X)
By = np.zeros_like(Y)
Bz = np.zeros_like(Z)

for i in range(len(theta)):
    # Vector from wire element to field point
    rx = X - radius * np.cos(theta[i])
    ry = Y - radius * np.sin(theta[i])
    rz = Z - 0
    
    # Distance from wire element to field point squared
    r_mag_squared = rx**2 + ry**2 + rz**2
    r_mag = np.sqrt(r_mag_squared)
    
    # Differential length element in direction of current (dL = R dθ (-sin(θ), cos(θ), 0))
    dLx = -radius * np.sin(theta[i]) * (theta[1] - theta[0])
    dLy = radius * np.cos(theta[i]) * (theta[1] - theta[0])
    dLz = 0
    
    # Cross product dL x r
    dL_cross_r_x = dLy * rz - dLz * ry
    dL_cross_r_y = dLz * rx - dLx * rz
    dL_cross_r_z = dLx * ry - dLy * rx
    
    # Add contribution from each segment to the magnetic field at each point
    Bx += mu_0 / (4 * np.pi) * (I * dL_cross_r_x / r_mag_squared**1.5)
    By += mu_0 / (4 * np.pi) * (I * dL_cross_r_y / r_mag_squared**1.5)
    Bz += mu_0 / (4 * np.pi) * (I * dL_cross_r_z / r_mag_squared**1.5)

# Plot the magnetic field vectors
ax.quiver(X, Y, Z, Bx, By, Bz, color='g', length=0.5, normalize=True, alpha=0.5, label="Magnetic field")

# Set labels and show plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Magnetic field visualization")
plt.show()
