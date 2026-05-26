## Week 2: Airfoil Selection & 2D Analysis

### Candidate Airfoils Evaluated
1. **NACA 2412**: General aviation baseline profile.
2. **Selig S7012**: High-speed, low-drag penetration profile.
3. **Drela AG35**: Specialized low-Reynolds-number soaring profile.

### Simulation Parameters
* **Software**: XFLR5 v6.62
* **Analysis Type**: XFoil Direct Analysis (Type 1)
* **Reynolds Number (Re)**: 100,000 (Simulating 2.0m glider cruise velocity)
* **Angle of Attack ($\alpha$) Sweep**: -5.0° to 15.0° (Step: 0.5°)

### Head-to-Head Performance Matrix
| Airfoil Profile | Max Lift ($Cl_{max}$) | Stall Angle ($\alpha_{stall}$) | Aerodynamic Stall Characteristic |
| :--- | :---: | :---: | :--- |
| **NACA 2412** | ~1.25 | 10.5° | Sharp, sudden loss of lift |
| **Selig S7012** | ~1.12 | 9.5° | Moderate drop-off, built for high speed |
| **Drela AG35** | **1.228** | **9.0°** | **Gentle, rounded peak (High recovery safety)** |

### Design Selection & Justification
The **Drela AG35** was officially selected as the primary wing airfoil for this aerospace portfolio project. 

While the NACA 2412 achieves a slightly higher absolute peak lift, it suffers from a sharp stall drop-off that presents high risks for low-altitude RC flight maneuvers. The Selig S7012 minimizes drag at high speeds but fails to generate the high lift coefficients required for slow, unpowered thermal soaring. 

The **Drela AG35** represents the optimal "Goldilocks" compromise for an endurance glider operating at $Re = 100,000$:
1. It delivers a high operating lift coefficient ($Cl = 1.228$) at a $9.0°$ angle of attack.
2. It exhibits a remarkably safe, progressive stall profile, allowing camp operators/hobby pilots ample time to recover before a total loss of control.
3. It maintains a tight profile against the low-drag boundary across the entire cruise lift spectrum.