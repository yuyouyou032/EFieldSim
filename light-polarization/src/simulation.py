import numpy as np

class EMWave:
    """Electromagnetic wave with defined amplitude, frequency, phase and polarization"""
    def __init__(self, amplitude, frequency, phase=0, direction='x'):
        """
        Parameters:
        -----------
        amplitude : float
            Peak amplitude of the wave
        frequency : float
            Angular frequency (ω) in rad/s
        phase : float
            Phase offset in radians
        direction : str
            Polarization direction ('x' or 'y')
        """
        self.A = amplitude
        self.omega = frequency
        self.lambda_ = 2 * np.pi / frequency
        self.phi = phase
        self.direction = direction

    def get_field(self, t):
        """Calculate E-field at time t"""
        return self.A * np.cos(self.omega * t + self.phi)

class PolarizedLight:
    """Superposition of EM waves to create different polarization states"""
    def __init__(self, Ex_wave, Ey_wave):
        """
        Parameters:
        -----------
        Ex_wave, Ey_wave : EMWave
            Component waves in x and y directions
        """
        self.Ex = Ex_wave
        self.Ey = Ey_wave

    def get_total_field(self, t):
        """Get total E-field vector at time t"""
        Ex = self.Ex.get_field(t)
        Ey = self.Ey.get_field(t)
        return np.array([Ex, Ey, 0])  # Adding z=0 for 3D visualization

    def get_polarization_type(self):
        """Determine type of polarization based on wave parameters"""
        if self.Ex.A == self.Ey.A:
            phase_diff = abs(self.Ey.phi - self.Ex.phi) % (2*np.pi)
            if np.isclose(phase_diff, np.pi/2):
                return "circular"
            else:
                return "elliptical"
        else:
            if self.Ex.A == 0 or self.Ey.A == 0:
                return "linear"
            else:
                return "elliptical"
            


def create_circular_polarization(amplitude=1.0, frequency=1.0):
    """Create circularly polarized light"""
    Ex = EMWave(amplitude, frequency, 0, 'x')
    Ey = EMWave(amplitude, frequency, np.pi/2, 'y')  # π/2 phase difference
    return PolarizedLight(Ex, Ey)

def create_elliptical_polarization(amplitude_x=1.0, amplitude_y=0.5, frequency=1.0, phase_diff=np.pi/4):
    """Create elliptically polarized light"""
    Ex = EMWave(amplitude_x, frequency, 0, 'x')
    Ey = EMWave(amplitude_y, frequency, phase_diff, 'y')
    return PolarizedLight(Ex, Ey)

def create_linear_polarization(amplitude=1.0, frequency=1.0, angle=0):
    """Create linearly polarized light at given angle"""
    Ex = EMWave(amplitude * np.cos(angle), frequency, 0, 'x')
    Ey = EMWave(amplitude * np.sin(angle), frequency, 0, 'y')
    return PolarizedLight(Ex, Ey)


