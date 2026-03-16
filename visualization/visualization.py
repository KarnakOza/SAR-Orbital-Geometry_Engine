import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ground target
ground = np.array([6378.0, 0.0, 0.0])
swath_width = 300   # km

# Orbit parameters
orbit_radius = 7071
inclination = np.radians(98)

theta = np.linspace(0, 2*np.pi, 300)

orbit_x = orbit_radius * np.cos(theta)
orbit_y = orbit_radius * np.sin(theta) * np.cos(inclination)
orbit_z = orbit_radius * np.sin(theta) * np.sin(inclination)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])

# Earth sphere
R = 6378
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = R*np.outer(np.cos(u), np.sin(v))
y = R*np.outer(np.sin(u), np.sin(v))
z = R*np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, color='lightblue', alpha=0.3, edgecolor='none')

# Plot orbit
ax.plot(orbit_x, orbit_y, orbit_z, color="orange", linewidth=2)

# Ground point
ax.scatter(ground[0], ground[1], ground[2], color='green', s=100, label="Ground Target")

# Ground track
ground_track_x = R * orbit_x / orbit_radius
ground_track_y = R * orbit_y / orbit_radius
ground_track_z = R * orbit_z / orbit_radius

ax.plot(ground_track_x, ground_track_y, ground_track_z,
        color="purple", linewidth=2, label="Ground Track")

# Animated satellite and radar beam
sat_point, = ax.plot([], [], [], 'ro', markersize=8, label="Satellite")
beam_line, = ax.plot([], [], [], color='orange', linewidth=2)
swath_line_left, = ax.plot([], [], [], color='cyan', linewidth=2)
swath_line_right, = ax.plot([], [], [], color='cyan', linewidth=2)

# Animation update function
def update(frame):

    sx = orbit_x[frame]
    sy = orbit_y[frame]
    sz = orbit_z[frame]

    sat_point.set_data([sx], [sy])
    sat_point.set_3d_properties([sz])

    beam_line.set_data([sx, ground[0]], [sy, ground[1]])
    beam_line.set_3d_properties([sz, ground[2]])

    # approximate swath edges

    swath_left = ground + np.array([0, swath_width/2, 0])
    swath_right = ground - np.array([0, swath_width/2, 0])

    swath_line_left.set_data([sx, swath_left[0]],
                         [sy, swath_left[1]])

    swath_line_left.set_3d_properties([sz, swath_left[2]])

    swath_line_right.set_data([sx, swath_right[0]],
                          [sy, swath_right[1]])

    swath_line_right.set_3d_properties([sz, swath_right[2]])

    return sat_point, beam_line, swath_line_left, swath_line_right

ani = FuncAnimation(fig, update, frames=len(theta), interval=50, blit=False)

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title("SAR Satellite Observation Geometry")

ax.legend()

plt.show()
