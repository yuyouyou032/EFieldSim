from simulation import create_circular_polarization, create_elliptical_polarization, create_linear_polarization
from visualization import PolarizationVisualizer
import numpy as np

class Crystal:
    """Class to represent an EO crystal under electric field"""
    def __init__(self, E_amp, E_dir, n_matrix=None, r_voigt_matrix=None):
        """
        Parameters:
        -----------
        E_amp : float
            Amplitude of the electric field
        E_dir : str
            Direction of the electric field (vector, numpy array)
        """
        self.E_amp = E_amp
        self.E_dir = np.array(E_dir)
        self.r_voigt_matrix = r_voigt_matrix if r_voigt_matrix is not None else np.zeros((6,3))
        self.n_matrix = n_matrix if n_matrix is not None else np.ones((3,1)) # Nx, Ny, Nz refractive indices 

    def get_r_voigt_matrix(self):
        """Get the Voigt matrix for the crystal"""
        return self.r_voigt_matrix

    def set_r_voigt_matrix(self, r_voigt_matrix):
        """Set the Voigt matrix for the crystal"""
        self.r_voigt_matrix = r_voigt_matrix   

    def EO_effect(self, E_field):
        """Calculate the electro-optic effect based on the electric field"""
        return self.r_voigt_matrix @ E_field # E field with a dimension of 3x1
