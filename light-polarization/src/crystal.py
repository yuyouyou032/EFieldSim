from simulation import create_circular_polarization, create_elliptical_polarization, create_linear_polarization
from visualization import PolarizationVisualizer
from simulation import EMWave, PolarizedLight
import numpy as np

class Crystal:
    """Class to represent an EO crystal under electric field"""
    def __init__(self, thickness=500e-6, n_matrix=None, r_voigt_matrix=None):
        """
        Parameters:
        -----------
        thickness : float (m)
            Thickness of the crystal
        n_matrix : np.ndarray
            Refractive index matrix
        r_voigt_matrix : np.ndarray
            Voigt matrix for the crystal
        E_dir : str
            Direction of the electric field (vector, numpy array)
        """
        self.thickness = thickness
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
            [0, 0, 0],
            [0, 0, 0],
            [r13, r13, r33],
            [0, r22, 0],
            [r22, 0, 0],
            [r51, 0, 0]
        ])

        r_voigt *= 1e-12

        # r_voigt = r_voigt.reshape(6, 3)

        self.r_voigt_matrix = r_voigt      

    def EO_effect(self, light: PolarizedLight, e = np.array([1, 0, 0]), E=1e5):
        """Calculate the electro-optic effect based on the electric field,
        returns a 6*1 vector"""
        r_voigt = self.r_voigt_matrix

        # Map Voigt to full tensor indices
        voigt_to_full = {
            0: (0, 0),
            1: (1, 1),
            2: (2, 2),
            3: (1, 2),
            4: (0, 2),
            5: (0, 1)
        }
        Delta_inv_eps = np.zeros((3, 3))
        for m in range(6):
            i, j = voigt_to_full[m]
        
            Delta_inv_eps[i, j] += r_voigt[m, 2] * E  # E_z = column 2
            if i != j:
                Delta_inv_eps[j, i] += r_voigt[m, 2] * E  # symmetric part
            
            print(Delta_inv_eps)
            print()

        Ex = np.array([light.Ex.get_field(0), 0, 0])  # Get E-field at t=0
        Ey = np.array([0, light.Ey.get_field(0), 0])  # Get E-field at t=0

        delta_inv_n2_x = Ex.T @ Delta_inv_eps @ Ex
        delta_inv_n2_y = Ey.T @ Delta_inv_eps @ Ey

        no = self.n_matrix[0]
        ne = self.n_matrix[2]

        print("no, ne:", no, ne)

        delta_n_eff_x = -0.5 * no**3 * delta_inv_n2_x
        delta_n_eff_y = -0.5 * ne**3 * delta_inv_n2_y
        print(delta_n_eff_x, delta_n_eff_y)

        delta_phi_x = (2 * np.pi / light.Ex.lambda_) * delta_n_eff_x * self.thickness
        delta_phi_y = (2 * np.pi / light.Ey.lambda_) * delta_n_eff_y * self.thickness


        # dummy
        delta_phi_x = 0.1
        delta_phi_y = 0.2
        return delta_phi_x, delta_phi_y
