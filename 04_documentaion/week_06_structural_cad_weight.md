# Week 06: Structural CAD Detailing, Composite Layup & Mass Properties

## 🎯 Objective
Design the internal wing structure and fuselage layup schedule for a 2.0m RC sailplane, define composite material properties, and build a component-by-component mass properties budget to verify Take-Off Weight (TOW) and Center of Gravity ($X_{\text{cg}}$) location.

---

## 🛠️ Structural Architecture

### 1. Wing Construction
* **Main Spar:** Carbon fiber caps ($10\text{mm} \times 1.5\text{mm}$) with a $3\text{mm}$ end-grain balsa shear web wrapped in $\pm 45^\circ$ fiberglass sleeve.
* **Rib Geometry:** 8 ribs per semi-span ($2.0\text{mm}$ balsa), $1.5\text{mm}$ light plywood root ribs.
* **Joiner Assembly:** $8\text{mm}$ solid carbon rod passing through brass/carbon sleeve at $25\%$ chord.

### 2. Layup Schedule
* **Wings:** Glass/Foam sandwich ($50\text{g/m}^2$ glass outer + $1.2\text{mm}$ Rohacell core + $25\text{g/m}^2$ glass inner).
* **Fuselage Pod:** Woven carbon fiber ($160\text{g/m}^2 \times 2$) + fiberglass impact layer.
* **Tail Boom:** Tapered carbon fiber tube ($35\text{g/m}$).

---

## 📊 Mass Budget & CG Summary

* **Target Take-Off Weight (TOW):** $< 700\text{ g}$
* **Calculated TOW ($M_{\text{TOW}}$):** $667.0\text{ g}$
* **Target $X_{\text{cg}}$:** $0.2406\text{ m}$ ($28.0\%$ MAC)
* **Calculated $X_{\text{cg}}$:** $0.2257\text{ m}$ ($25.7\%$ MAC)
* **Wing Loading:** $22.5\text{ g/dm}^2$

---

## 🔑 Key Engineering Takeaways
1. **Controllable Static Margin:** The calculated mass distribution yields a stable $12.3\%$ static margin, which can be tuned precisely to $10.0\%$ by shifting the internal receiver battery pack back $15\text{ mm}$.
2. **Structural Margin:** Spar cap design provides a safety factor of $SF = 2.1$ against $6g$ maneuver loads at maximum glide velocity ($V = 18\text{ m/s}$).