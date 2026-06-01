# Week 3: Initial 3D Wing Aerodynamic Modeling

## Objective
To transition from 2D airfoil analysis to a 3D wing structure by establishing a baseline configuration using the Vortex Lattice Method (VLM1) in XFLR5. This rectangular wing serves as the project's aerodynamic control group; all subsequent design iterations (taper, twist, winglets) will be evaluated against these baseline metrics to measure drag reduction and efficiency gains.

## Baseline Design Specifications
The geometry was constrained to a standard rectangular planform to isolate 3D induced wingtip effects from complex planform variables.

| Parameter | Value | Engineering Rationale |
| :--- | :--- | :--- |
| **Airfoil Profile** | NACA 4412 | Selected from Week 2 evaluation for optimal high-camber performance. |
| **Total Wingspan ($b$)** | 2.0 m | Primary physical constraint for the glider project scale. |
| **Chord Line ($c$)** | 0.20 m | Constant from root to tip (Taper Ratio $\lambda = 1.0$). |
| **Aspect Ratio ($AR$)** | 10.00 | Calculated via $AR = b / c$. High-efficiency baseline baseline. |
| **Wing Sweep / Offset** | 0.00 m | Straight leading edge (0.00°) to minimize torsional spar loading. |
| **Dihedral Angle** | 0.0° | Perfectly planar configuration to establish pure aerodynamic baseline. |

---

## Aerodynamic Simulation Methodology
* **Analysis Engine:** XFLR5 v6.62 
* **Methodology:** Vortex Lattice Method (VLM1)
* **Inflow Boundaries:** Fixed Speed ($V_{\infty} = 10.0 \text{ m/s}$)
* **Angle of Attack Range:** $\alpha = -5.0^\circ$ to $+11.0^\circ$ (Step $\Delta = 0.5^\circ$)
* **Mesh Density:** 900 VLM Panels total (15 X-panels $\times$ 30 Y-panels per wing half)

### Numerical Solver Calibration
During initial execution, the 3D solver encountered interpolation failures (`outside the flight envelope of polars`) due to localized high lift coefficients ($C_l \approx 1.66 - 1.73$) out near the wingtips operating at a local Reynolds number of approximately $Re = 133,333$. 

The solver was successfully stabilized by regenerating the 2D NACA 4412 polar envelope in the Direct Foil Design module at a higher boundary of $Re = 150,000$, extending the maximum 2D simulation range to $\alpha = 20.0^\circ$. This expanded the lookup envelope sufficiently for the 3D multi-panel matrix solver to converge.

---

## Performance Results & Baseline Data
The optimum cruise state was isolated at **$\alpha = 4.00^\circ$**, which corresponds exactly to the peak of the 3D Lift-to-Drag efficiency curve ($L/D_{max}$). 



The absolute baseline values recorded at this cruise state are:

* **Cruise Angle of Attack ($\alpha$):** $4.00^\circ$
* **Total 3D Lift Coefficient ($C_L$):** $0.679$
* **Total 3D Drag Coefficient ($C_D$):** $0.030$
* **Pitching Moment Coefficient ($C_m$):** $-0.274$ 
* **Maximum 3D Glide Efficiency ($L/D$):** $22.63$

---

## Aerodynamic Analysis & Critical Takeaway



The core finding of Week 3 highlights the steep "aerodynamic tax" imposed by moving from a 2D infinite wing slice to a physical 3D lifting surface. While the isolated 2D NACA 4412 profile yielded an ideal glide ratio exceeding **55**, the bound 3D baseline wing efficiency dropped significantly to **22.63**. 

This performance reduction is directly driven by **induced drag ($C_{Di}$)**. High-pressure air beneath the flat, rectangular wingtip spills over into the low-pressure zone on top, generating continuous tip vortices. These vortices induce a downward velocity component (downwash) on the oncoming airflow, tilting the net lift vector backwards and introducing an ongoing drag penalty. 

## Next Steps: Week 4 Optimization Goals
With the control group metrics successfully locked in, the design focus shifts to lowering the baseline drag coefficient ($C_D = 0.030$). Future modifications will target:
1. **Elliptical Lift Distribution:** Introducing a tapered planform ($\lambda < 1.0$) to optimize spanwise loading.
2. **Geometric Washout:** Incorporating a negative aerodynamic twist at the tips to mitigate premature stall and minimize tip vortex intensity.