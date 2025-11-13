import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from simulation import create_circular_polarization, create_elliptical_polarization, create_linear_polarization
from visualization import PolarizationVisualizer
from crystal import Crystal
import numpy as np

def compute_geometry(Params):
    # Create different types of polarized light
    # # 1. Circular polarization
    # circular_light = create_circular_polarization(
    #     amplitude=1.0,
    #     frequency=2*np.pi  # ω = 2π for 1 Hz
    # )
    
    # # 2. Elliptical polarization
    # elliptical_light = create_elliptical_polarization(
    #     amplitude_x=1.0,
    #     amplitude_y=0.5,
    #     frequency=2*np.pi,
    #     phase_diff=np.pi/4
    # )
    
    # # 3. Linear polarization at 45 degrees
    # linear_light = create_linear_polarization(
    #     amplitude=1.0,
    #     frequency=2*np.pi,
    #     angle=np.pi/4
    # )
    
    # Visualize each type
    # for light, name in [(circular_light, "Circular"),
    #                    (elliptical_light, "Elliptical"),
    #                    (linear_light, "Linear")]:
    #     print(f"\nVisualizing {name} Polarization:")


    c = Crystal()
    c.set_liNbO3_refractive_index_1550()  # Example
    c.set_r_voigt_matrix_LiNbO3()  # Set Voigt matrix for LiNbO3


    amplitude_x=Params.get("amplitude_x", 1.0) # is that really okay?
    amplitude_y=Params.get("amplitude_y", 1.0)
    frequency=Params.get("frequency", 2*np.pi)
    phase_diff=Params.get("phase_diff", 0)
    print("amplitude:", amplitude_x, amplitude_y, "frequency:", frequency, "Phase difference:", phase_diff)

# elliptically polarised light
    light = create_elliptical_polarization(
    amplitude_x=amplitude_x,
    amplitude_y=amplitude_y,
    frequency=frequency,
    phase_diff=phase_diff
    )
# resultant phase shifted light after EO effect
    a, b = c.EO_effect(light)
# and also: at this stage you only need to compute phase shift once...

# visualise resultant light
    resultant_light = create_elliptical_polarization(
    amplitude_x=amplitude_x,
    amplitude_y=amplitude_y,
    frequency=frequency,
    phase_diff=np.abs(a[0]-b[0])
    )
    

    # viz = PolarizationVisualizer(light, t_max=2, fps=30)
    
    # Show 3D animation
    # viz.plot_components()
    

    # print("v-matrix", c.get_r_voigt_matrix())
    # print("E-field components:", light.Ex.A, light.Ey.A)
    
    
    # Show components
    # viz.plot_components()
    
    # # Show polarization ellipse
    # viz.plot_polarization_ellipse()

    # print("DEBUGGING MESSAGES:")
    # print(a, b, light.Ex.get_field(0), light.Ey.get_field(0))
    # print(light.get_polarization_type(), light.Ex.A, light.Ey.A, abs(a[0]-b[0]))
    
    return {
        "delta_phi_1":a[0], 
        "delta_phi_2":b[0],
        "resultantEx":[resultant_light.Ex.get_field(t) for t in np.linspace(0, 2*np.pi, num=100)],
        "resultantEy":[resultant_light.Ey.get_field(t) for t in np.linspace(0, 2*np.pi, num=100)],
        "meta":{
            "crystal": "LiNbO3",
            "frequency": resultant_light.Ex.f,
            "resultant_polarization": resultant_light.get_polarization_type(),
            "input_amplitudes": (light.Ex.A, light.Ey.A),
        }

    }

if __name__ == "__main__":
    compute_geometry()