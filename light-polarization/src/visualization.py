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
        
    # # def plot_3d_evolution(self):
    #     """Create 3D animation of E-field evolution showing x and y components separately"""
    #     fig = plt.figure(figsize=(12, 8))
    #     ax = fig.add_subplot(111, projection='3d')
        
    #     # Initialize lines and points for both components
    #     line_x, = ax.plot([], [], [], 'r-', lw=2, label='Ex component')  # x component
    #     line_y, = ax.plot([], [], [], 'b-', lw=2, label='Ey component')  # y component
    #     point_x, = ax.plot([], [], [], 'ro')
    #     point_y, = ax.plot([], [], [], 'bo')
        
    #     # Set axis limits and labels
    #     ax.set_xlim(-1.5, 1.5)
    #     ax.set_ylim(-1.5, 1.5)
    #     ax.set_zlim(-0.5, 0.5)
    #     ax.set_xlabel('E_x')
    #     ax.set_ylabel('E_y')
    #     ax.set_zlabel('z')
    #     ax.legend()
        
    #     def init():
    #         # Initialize both components
    #         line_x.set_data([], [])
    #         line_x.set_3d_properties([])
    #         line_y.set_data([], [])
    #         line_y.set_3d_properties([])
    #         point_x.set_data([], [])
    #         point_x.set_3d_properties([])
    #         point_y.set_data([], [])
    #         point_y.set_3d_properties([])
    #         return line_x, line_y, point_x, point_y
        
    #     def animate(i):
    #         # Calculate field for time window
    #         t = self.times[i]
    #         z = np.linspace(0, 0.3, 20)  # Propagation axis
            
    #         # Get current field values
    #         field = self.light.get_total_field(t)
            
    #         # Update x component (red)
    #         x_comp = np.ones_like(z) * field[0]
    #         y_comp_x = np.zeros_like(z)  # y=0 for x component
    #         line_x.set_data(x_comp, y_comp_x)
    #         line_x.set_3d_properties(z)
    #         point_x.set_data([0, field[0]], [0, 0])
    #         point_x.set_3d_properties([0, 0])
            
    #         # Update y component (blue)
    #         x_comp_y = np.zeros_like(z)  # x=0 for y component
    #         y_comp = np.ones_like(z) * field[1]
    #         line_y.set_data(x_comp_y, y_comp)
    #         line_y.set_3d_properties(z)
    #         point_y.set_data([0, 0], [0, field[1]])
    #         point_y.set_3d_properties([0, 0])
            
    #         return line_x, line_y, point_x, point_y
        
    #     anim = FuncAnimation(fig, animate, init_func=init,
    #                        frames=len(self.times), interval=self.dt*1000,
    #                        blit=True)
        
    #     plt.title(f'Polarization: {self.light.get_polarization_type()}')
    #     plt.show()
        

    def plot_3d_frame(self, t_total = 0.3, ts=20):
        """Plot a single 3D frame of the E-field components"""
        plt.ion()  # Enable interactive mode
        fig = plt.figure(figsize=(10, 8))
        
        ax = fig.add_subplot(111, projection='3d')
        t = self.times[:ts] 
        z = np.linspace(0, t_total, ts)  # Propagation axis

        # Get current field values
        ex_field = np.array([self.light.Ex.get_field(t) for t in self.times[:ts]])
        ey_field = np.array([self.light.Ey.get_field(t) for t in self.times[:ts]])
        total_field = np.sqrt(ex_field**2 + ey_field**2)

        # Plot E-field components
        for i in range(ts):
            ax.plot([0, ex_field[i]], [0, 0], [z[i], z[i]], 'r->', lw=2)
            ax.plot([0, 0], [0, ey_field[i]], [z[i], z[i]], 'b->', lw=2)
            ax.plot([0, ex_field[i]], [0, ey_field[i]], [z[i], z[i]], 'g->', lw=2)

        ax.set_xlabel('E_x')
        ax.set_ylabel('E_y')
        ax.set_zlabel('z')
        ax.set_title(f'Polarization: {self.light.get_polarization_type()}')
        ax.legend()

            # Enable mouse interaction
        ax.mouse_init()
        
        # Set consistent aspect ratio for better 3D visualization
        ax.set_box_aspect([1,1,1])
        
        # Optional: Set initial viewing angle
        ax.view_init(elev=20, azim=45)


        plt.show()
        # print(ex_field, ey_field, total_field)

        input("Press Enter to close the plot...")  # Keep plot window open




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