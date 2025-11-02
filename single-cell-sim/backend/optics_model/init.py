from simulation import create_circular_polarization, create_elliptical_polarization, create_linear_polarization
from visualization import PolarizationVisualizer
from crystal import Crystal
import numpy as np

def main():
    # Create different types of polarized light
    # 1. Circular polarization
    circular_light = create_circular_polarization(
        amplitude=1.0,
        frequency=2*np.pi  # ω = 2π for 1 Hz
    )
    
    # 2. Elliptical polarization
    elliptical_light = create_elliptical_polarization(
        amplitude_x=1.0,
        amplitude_y=0.5,
        frequency=2*np.pi,
        phase_diff=np.pi/4
    )
    
    # 3. Linear polarization at 45 degrees
    linear_light = create_linear_polarization(
        amplitude=1.0,
        frequency=2*np.pi,
        angle=np.pi/4
    )
    
    # Visualize each type
    # for light, name in [(circular_light, "Circular"),
    #                    (elliptical_light, "Elliptical"),
    #                    (linear_light, "Linear")]:
    #     print(f"\nVisualizing {name} Polarization:")


    c = Crystal()
    c.set_liNbO3_refractive_index_1550()  # Example
    c.set_r_voigt_matrix_LiNbO3()  # Set Voigt matrix for LiNbO3

    
# eleptically polarised light
    light = elliptical_light = create_elliptical_polarization(
    amplitude_x=1.0,
    amplitude_y=1,
    frequency=2*np.pi,
    phase_diff=0
    )
# resultant phase shifted light after EO effect
    a, b = c.EO_effect(light)
    print("Phase shifts:", a, b)

# visualise resultant light
    light = elliptical_light = create_elliptical_polarization(
    amplitude_x=1.0,
    amplitude_y=1,
    frequency=2*np.pi,
    phase_diff=np.abs(a[0]-b[0])
    )

    viz = PolarizationVisualizer(light, t_max=2, fps=30)
    
    # Show 3D animation
    viz.plot_3d_frame()
    

    # print("v-matrix", c.get_r_voigt_matrix())
    # print("E-field components:", light.Ex.A, light.Ey.A)
    
    
    # Show components
    # viz.plot_components()
    
    # # Show polarization ellipse
    # viz.plot_polarization_ellipse()

    return {
        "axis-1":a, 
        "axis-2":b,
        "resultant":light,
        "meta":{
            "crystal": "LiNbO3",
            "wavelength": light.get_polarization_type(),
            "input_amplitudes": (a.A, b.A),
            "input_phase_diff": np.abs(a[0]-b[0])
        }

    }



if __name__ == "__main__":
    main()