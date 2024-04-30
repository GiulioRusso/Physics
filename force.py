import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Rectangle

# Function to update the plot when sliders are moved
def update(val):
    ax.clear()
    ax.quiver(0, 0, 0, -5, angles='xy', scale_units='xy', scale=1, color='b', label='Force of gravity')
    ax.quiver(0, 0, slider_x.val, slider_y.val, angles='xy', scale_units='xy', scale=1, color='r', label='External Force')
    ax.quiver(0, 0, slider_x.val, slider_y.val - 5, angles='xy', scale_units='xy', scale=1, color='g', label='Resultant Force')
    ax.add_patch(Rectangle((-2.5, -2.5), 5, 5, color='lightgrey', alpha=0.5))
    ax.legend()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    plt.draw()

# Create initial plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Create sliders
ax_x = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_y = plt.axes([0.1, 0.05, 0.65, 0.03])
slider_x = Slider(ax_x, 'X', -10.0, 10.0, valinit=0)
slider_y = Slider(ax_y, 'Y', -10.0, 10.0, valinit=0)

# Attach update function to sliders
slider_x.on_changed(update)
slider_y.on_changed(update)

# Initial plot
update(None)

plt.show()
