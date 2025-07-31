import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

class PolarizationVisualizer:
    def __init__(self, polarized_light, t_max=10, fps=30):
        """
        Parameters:
        -----------
        polarized_light : PolarizedLight
            Light wave to visualize
        t_max : float
            Maximum time for animation in periods
        fps : int
            Frames per second for animation
        """
        self.light = polarized_light
        self.t_max = t_max
        self.dt = 1 / fps
        self.times = np.arange(0, t_max, self.dt)
        
    def plot_3d_evolution(self):
        """Create 3D animation of E-field evolution"""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Initialize line and point
        line, = ax.plot([], [], [], 'b-', lw=2)  # Field path
        point, = ax.plot([], [], [], 'ro')  # Current position
        
        # Set axis limits and labels
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_zlim(-0.5, 0.5)
        ax.set_xlabel('E_x')
        ax.set_ylabel('E_y')
        ax.set_zlabel('z')
        
        def init():
            line.set_data([], [])
            line.set_3d_properties([])
            point.set_data([], [])
            point.set_3d_properties([])
            return line, point
        
        def animate(i):
            # Calculate field for time window
            t = self.times[i]
            z = np.linspace(0, 0.3, 20)  # Propagation axis
            
            # Get current field values
            field = self.light.get_total_field(t)
            
            # Update line (showing propagation)
            x = np.ones_like(z) * field[0]
            y = np.ones_like(z) * field[1]
            line.set_data(x, y)
            line.set_3d_properties(z)
            
            # Update point (showing E-field vector)
            point.set_data([0, field[0]], [0, field[1]])
            point.set_3d_properties([0, 0])
            
            return line, point
        
        anim = FuncAnimation(fig, animate, init_func=init,
                           frames=len(self.times), interval=self.dt*1000,
                           blit=True)
        
        plt.title(f'Polarization: {self.light.get_polarization_type()}')
        plt.show()
        
    def plot_components(self):
        """Plot Ex and Ey components over time"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
        
        # Calculate fields
        Ex = [self.light.Ex.get_field(t) for t in self.times]
        Ey = [self.light.Ey.get_field(t) for t in self.times]
        
        # Plot Ex
        ax1.plot(self.times, Ex)
        ax1.set_ylabel('Ex')
        ax1.grid(True)
        
        # Plot Ey
        ax2.plot(self.times, Ey)
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Ey')
        ax2.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def plot_polarization_ellipse(self):
        """Plot the polarization ellipse"""
        Ex = [self.light.Ex.get_field(t) for t in self.times]
        Ey = [self.light.Ey.get_field(t) for t in self.times]
        
        plt.figure(figsize=(8, 8))
        plt.plot(Ex, Ey)
        plt.xlabel('Ex')
        plt.ylabel('Ey')
        plt.title(f'Polarization Ellipse: {self.light.get_polarization_type()}')
        plt.axis('equal')
        plt.grid(True)
        plt.show()