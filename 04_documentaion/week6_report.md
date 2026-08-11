# Week 6: Parametric CAD Wing Design & Structural Disaggregation

## Overview
Modeled a tapered, twisted 3D wing structure in SolidWorks based on the NACA 4412 airfoil series. The workflow transitions from raw aerodynamic coordinate datasets to a lofted Outer Mold Line (OML), incorporates an internal structural spar channel along the quarter-chord axis, and utilizes multi-body features to isolate individual structural ribs across spanwise stations.

---

## Key Design Specifications

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Airfoil Profile** | NACA 4412 | 4% max camber at 40% chord, 12% max thickness |
| **Root Chord ($c_{\text{root}}$)** | $180\text{ mm}$ | Placed at $X = 0\text{ mm}$ (Root Plane) |
| **Tip Chord ($c_{\text{tip}}$)** | $110\text{ mm}$ | Placed at $X = 1000\text{ mm}$ (Plane 8) |
| **Semi-Span ($b/2$)** | $1000\text{ mm}$ | Distributed across 8 reference planes |
| **Geometric Washout** | $-2.0^\circ$ | Tip twist applied around $25\%$ quarter-chord axis |
| **Main Spar Channel** | $\varnothing 8.0\text{ mm}$ | Swept along the $25\%$ quarter-chord axis |
| **Rib Count** | 8 Bodies | Disaggregated using the SolidWorks `Split` feature |

---

## Workflow & Implementation Steps

### 1. Datum Plane & Coordinate Setup
- Generated 8 reference planes along the span to define internal rib stations.
- Formatted NACA 4412 coordinate files mapped to SolidWorks global coordinates ($X$ = spanwise, $Y$ = vertical thickness, $Z$ = chordwise).
- Imported root and tip profiles using **Curve Through XYZ Points**.

### 2. Aerodynamic Twist & Outer Mold Line Loft
- Applied a $-2.0^\circ$ nose-down geometric rotation to the tip profile at $25\%$ chord to mitigate tip-stall tendencies under high angle of attack ($AoA$).
- Executed a multi-profile **Lofted Boss/Base** between `Curve1` and `Sketch1` to form the continuous outer skin surface (`Loft1`).

### 3. Structural Axis & Swept Spar Channel
- Defined a $25\%$ quarter-chord centerline (`Sketch5`) across the Top Plane linking $Z = 45\text{ mm}$ (root) to $Z = 27.5\text{ mm}$ (tip).
- Constructed an $\varnothing 8.0\text{ mm}$ circular profile on the Right Plane and executed a **Swept Cut** along the quarter-chord guide path to generate a continuous joiner tube passage.

### 4. Multi-Body Rib Disaggregation
- Applied the **Split** tool using reference planes (`Plane1` through `Plane7`) as trim tools.
- Divided `Loft1` into 8 discrete solid bodies in the FeatureManager tree, isolating individual rib geometries for subsequent detail design and manufacturing exports (DXF/STEP).

---

## Deliverables & Artifacts
- `NACA4412_Wing.SLDPRT`: Parametric SolidWorks part file.
- `naca4412_root.txt` / `naca4412_tip.txt`: XYZ coordinate datasets.
- Screenshots documenting feature tree hierarchy and multi-body split results.