import plotly.graph_objects as go
import numpy as np

# Refractive indices (approximate at 633 nm)
n_x = 2.286  # Ordinary ray
n_y = 2.286  # Ordinary ray (uniaxial, so same as x)
n_z = 2.200  # Extraordinary ray

# Axis unit vectors (crystallographic: x=a, y=b, z=c)
axes = {
    'x (a-axis)': (1, 0, 0),
    'y (b-axis)': (0, 1, 0),
    'z (c-axis)': (0, 0, 1)
}
refractive_indices = {
    'x (a-axis)': n_x,
    'y (b-axis)': n_y,
    'z (c-axis)': n_z
}

# Create 3D quiver plot for axes
fig = go.Figure()

for label, direction in axes.items():
    n = refractive_indices[label]
    fig.add_trace(go.Scatter3d(
        x=[0, direction[0]],
        y=[0, direction[1]],
        z=[0, direction[2]],
        mode='lines+text',
        line=dict(width=10),
        text=[None, f'{label}<br>n = {n}'],
        textposition='top center',
        name=label
    ))

# Add symmetry triangle to indicate 3-fold rotation symmetry around z
theta = np.linspace(0, 2 * np.pi, 4)[:-1]
radius = 0.5
x_sym = radius * np.cos(theta)
y_sym = radius * np.sin(theta)
z_sym = np.zeros_like(x_sym)

fig.add_trace(go.Mesh3d(
    x=x_sym,
    y=y_sym,
    z=z_sym,
    color='lightblue',
    opacity=0.3,
    name='3-fold symmetry plane'
))

# Layout adjustments
fig.update_layout(
    scene=dict(
        xaxis=dict(title='x (a-axis)', range=[-1, 1]),
        yaxis=dict(title='y (b-axis)', range=[-1, 1]),
        zaxis=dict(title='z (c-axis)', range=[-1, 1]),
        aspectmode='cube'
    ),
    title='3D Visualization of Lithium Niobate Axes and Refractive Indices',
    showlegend=False
)

import plotly.io as pio
pio.renderers.default = 'browser'  # This opens it in your default web browser
fig.show()