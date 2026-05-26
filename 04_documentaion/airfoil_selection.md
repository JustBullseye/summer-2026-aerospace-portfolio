## Week 2: Airfoil Selection & Python Data Analysis

### Candidate Airfoils Evaluated
1. **NACA 2412**: General aviation baseline profile.
2. **S1223**: High-lift, heavy-payload cambered profile.
3. **S7012**: High-speed penetration profile.
4. **AG35**: Low-Reynolds specialized soaring profile.
5. **NACA 4412**: High-camber aerodynamic profile.

### Simulation & Plotting Parameters
* **Aerodynamic Engine**: XFLR5 v6.62 (Type 1 Analysis, $Re = 100,000$)
* **Data Processing**: Python 3.14 (Pandas, Matplotlib)
* **Target Metric**: Lift-to-Drag Ratio ($L/D$) vs Angle of Attack ($\alpha$)

### Python-Generated Performance Plot
![Airfoil Glide Efficiency Comparison](01_aerodynamics/polars/airfoil_comparison_plot.png)

### Performance Evaluation Matrix
* **Maximum Glide Efficiency ($L/D_{max}$)**: NACA 4412 ($L/D \approx 55.5$ @ $\alpha = 9.0^\circ$)
* **Broad-Range Cruise Stability**: NACA 4412 maintains the highest efficiency from $\alpha = 7.5^\circ$ to $15^\circ$.
* **High-Lift Constraint**: While the S1223 (Orange) offers exceptional early lift generation, its heavy drag profile drastically reduces glide performance beyond $\alpha = 5^\circ$.

### Engineering Decision
The **NACA 4412** is selected as the primary wing geometry. It definitively satisfies our mission requirements by offering the maximum aerodynamic glide efficiency ($L/D > 55$) at a stable, controllable angle of attack. This ensures excellent thermal soaring capabilities and maximal range for our 2.0-meter platform.