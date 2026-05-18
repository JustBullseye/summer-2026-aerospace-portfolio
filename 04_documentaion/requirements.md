# Project Mission & Technical Requirements Study
**Project Name:** Optimized RC Glider Design Study & Performance Simulator  
**Author:** Pranate Nadkarni  
**Timeline:** Summer 2025 (May 20 – August 22)  
**Target Audience:** Undergraduate Portfolio / Pathway to AERSP 204H Honors  

---

## 1. Project Mission Statement
The objective of this independent research project is to execute the complete conceptual, aerodynamic, and structural design of a high-performance, 2.0-meter radio-controlled (RC) sailplane. This design study aims to bridge the gap between abstract aerodynamic theory and practical flight vehicle design. Every design iteration will be driven by parametric analysis and automated data-processing workflows, culminating in a physics-based Python flight simulator and a manufacturing-ready SolidWorks CAD assembly. 

Ultimately, this project serves as technical preparation for the Penn State AERSP 204H Honors pathway and demonstrates the self-directed technical depth required for junior-level aerospace engineering internships.

---

## 2. Top-Level Performance & Operational Requirements
To ensure the aircraft is competitive, legal for RC sailplane competitions, and aerodynamically optimized for pure soaring, the vehicle must meet the following quantitative engineering targets:

| Parameter | Target Value | Engineering Justification |
| :--- | :--- | :--- |
| **Wingspan (b)** | ~2.0 m | Standard RC competition-legal scale; manageable structural footprint for a sophomore design project. |
| **Target Glide Ratio (L/D)** | > 25:1 | Matches high-performance RC glider benchmarks; demands rigorous minimization of induced and parasitic drag. |
| **Wing Loading** | 8 - 12 oz/ft² | Balances low-speed thermalling capabilities with the penetration speed necessary to fly through headwinds. |
| **Configuration** | Conventional T-tail or V-tail | Maximizes aerodynamic efficiency; protects the horizontal stabilizer from ground-effect damage during landings. |
| **Structural Frame** | Composite skin over balsa/carbon frame | Provides a realistic engineering constraint for structural deflection and weight budget calculations. |

---

## 3. Toolchain & Workflow Execution
To mirror professional aerospace workflows, the project explicitly rejects arbitrary design choices in favor of a data-driven pipeline:

1. **Aerodynamic Analysis (XFLR5):** Employ Vortex Lattice Method (VLM) sweeps to compare 4-5 candidate airfoils and evaluate 3D wing planforms.
2. **Computational Automation (Python):** Automate XFLR5 output parsing and run a 50+ parametric point Design of Experiments (DoE) to optimize aspect ratio, taper, and washout.
3. **3D Parametric Modeling (OpenVSP):** Generate full-aircraft NASA OpenVSP geometry to compute tail volume coefficients and verify static stability.
4. **Structural CAD (SolidWorks):** Import optimized outer mold lines to design internal wing architecture, including spar sizing for an estimated 2g load.
5. **Numerical Simulation (Python):** Build a parallel computational flight tool executing MacCready speed-to-fly algorithms and cross-country range estimations.