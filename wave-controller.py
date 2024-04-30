import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Create initial sine wave parameters
amplitude_initial = 1.0
frequency_initial = 1.0
phase_initial = 0.0

# Generate x values
x = np.linspace(0, 2 * np.pi, 1000)

# Calculate y values for the sine wave
y_initial = amplitude_initial * np.sin(frequency_initial * x + phase_initial)

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Plot the initial sine wave
line, = ax.plot(x, y_initial, lw=2, color='blue')

# Initialize dashed line for peaks and amplitude
peak_line, = ax.plot([], [], 'r--', lw=1.5, label="Wavelength")
amplitude_line, = ax.plot([], [], 'g--', lw=1.5, label="Amplitude")

# Create sliders for controlling the parameters
ax_amplitude = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_frequency = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_phase = plt.axes([0.2, 0.05, 0.65, 0.03])

slider_amplitude = Slider(ax_amplitude, 'Amplitude', 0.1, 2.0, valinit=amplitude_initial)
slider_frequency = Slider(ax_frequency, 'Frequency', 0.1, 10.0, valinit=frequency_initial)
slider_phase = Slider(ax_phase, 'Phase', 0.0, 2 * np.pi, valinit=phase_initial)

# Function to update plot
def update(val):
    amplitude = slider_amplitude.val
    frequency = slider_frequency.val
    phase = slider_phase.val

    # Calculate y values for the sine wave
    y = amplitude * np.sin(frequency * x + phase)
    line.set_ydata(y)

    # Calculate first positive peak position
    peak_x1 = (np.pi/2 - phase) / frequency
    peak_x2 = (4*np.pi/2 - phase) / frequency

    # Ensure the peaks are within the plot range
    while peak_x1 > max(x):
        peak_x1 -= 2 * np.pi / frequency
    while peak_x1 < min(x):
        peak_x1 += 2 * np.pi / frequency

    while peak_x2 > max(x):
        peak_x2 -= 2 * np.pi / frequency
    while peak_x2 < min(x):
        peak_x2 += 2 * np.pi / frequency

    # Update dashed line data
    peak_y = [amplitude, amplitude]  # Peak heights are at amplitude
    peak_line.set_data([peak_x1, peak_x1 + peak_x2], peak_y)

    amplitude_line.set_data([peak_x1, peak_x1], [0, amplitude])

    # Redraw the plot
    fig.canvas.draw_idle()

# Attach update function to sliders
slider_amplitude.on_changed(update)
slider_frequency.on_changed(update)
slider_phase.on_changed(update)

# Set plot attributes
plt.xlabel('X')
plt.ylabel('Y')
ax.set_title('Sine Wave')
ax.legend()

# Show the plot
plt.show()
