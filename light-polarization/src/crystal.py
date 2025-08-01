from simulation import create_circular_polarization, create_elliptical_polarization, create_linear_polarization
from visualization import PolarizationVisualizer
import numpy as np

class Crystal:
    """Class to represent an EO crystal under electric field"""
    def __init__(self, n_matrix=None, r_voigt_matrix=None):
        """
        Parameters:
        -----------
        E_amp : float
            Amplitude of the electric field
        E_dir : str
            Direction of the electric field (vector, numpy array)
        """
        self.r_voigt_matrix = r_voigt_matrix if r_voigt_matrix is not None else np.zeros((6,3))
        self.n_matrix = n_matrix if n_matrix is not None else np.ones((3,1)) # Nx, Ny, Nz refractive indices 

    import numpy as np

    def set_liNbO3_refractive_index_1550(self):
        """
        Set the refractive index for LiNbO3 at 1550 nm wavelength. at 300K
        The refractive indices are taken from the literature.
        https://nano-optics.seas.harvard.edu/abc-0
        """



        no = 2.21
        ne = 2.14
        self.n_matrix = np.array([no, no, ne]).reshape(3, 1)


    def get_r_voigt_matrix(self):
        """Get the Voigt matrix for the crystal"""
        return self.r_voigt_matrix

    def set_r_voigt_matrix_LiNbO3(self):
        """Set the Voigt matrix for the crystal"""
        r13 = 10
        r22 = 6.8
        r33 = 32.2
        r51 = 32.0

        r_voigt = np.array([
            [0,    0,    0,     0,   r13, 0],
            [0,    0,    0,    r13,   0,  0],
            [r33, r33, r33,     0,   0,   0]
        ])

        r_voigt *= 1e-12

        r_voigt = r_voigt.reshape(6, 3)

        self.r_voigt_matrix = r_voigt       

    def EO_effect(self, E_field):
        """Calculate the electro-optic effect based on the electric field,
        returns a 6*1 vector"""
        r_voigt = r_voigt.reshape(6, 3)
        E_field = E_field.reshape(3, 1)
        return self.r_voigt_matrix @ E_field # E field with a dimension of 3x1
