import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters for the sinusoids
frequency = 1  # frequency of the sinusoids
amplitude1 = 1  # amplitude of the first sinusoid
amplitude2 = 1  # amplitude of the second sinusoid
phase1 = 0  # phase of the first sinusoid in radians
phase2 = 0  # phase of the second sinusoid in radians
x = np.linspace(0, 4*np.pi, 1000)  # x values

# Create the figure and axes
fig, ax = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.25, top=0.95, hspace=0.5)

# Function to update the plot based on the slider's value
def update(val):
    amp2 = slider_amp.val
    ph2 = slider_phase.val
    y1 = amplitude1 * np.sin(frequency * x + phase1)
    y2 = amp2 * np.sin(frequency * x + ph2)
    y_sum = y1 + y2

    for a in ax:
        a.clear()

    ax[0].plot(x, y1)
    ax[0].set_title('Sinusoid 1')
    ax[0].set_ylim(-4, 4)

    ax[1].plot(x, y2)
    ax[1].set_title('Sinusoid 2')
    ax[1].set_ylim(-4, 4)

    ax[2].plot(x, y_sum, label='Sum', color='red')
    ax[2].set_title('Sum (Interference Pattern)')
    ax[2].set_ylim(-4, 4)

    for a in ax:
        a.set_ylabel('Amplitude')

    ax[2].set_xlabel('x')
    fig.canvas.draw_idle()

# Sliders
axcolor = 'lightgoldenrodyellow'
ax_amp = plt.axes([0.22, 0.1, 0.6, 0.03], facecolor=axcolor)
ax_phase = plt.axes([0.22, 0.15, 0.6, 0.03], facecolor=axcolor)

slider_amp = Slider(ax_amp, 'Amplitude 2', 0.1, 2.0, valinit=amplitude2)
slider_phase = Slider(ax_phase, 'Phase 2 (radians)', -np.pi, np.pi, valinit=phase2)

slider_amp.on_changed(update)
slider_phase.on_changed(update)

# Initial update
update(None)

plt.show()
