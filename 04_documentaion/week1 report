# Week 01: Airfoil Selection & 2D XFOIL Analysis

## 🎯 Objective
Evaluate 2D aerodynamic characteristics for low-Reynolds-number flight regimes ($Re \approx 100,000 \text{ to } 300,000$), compare candidate airfoils, and select a high-lift, moderate-camber profile for a small fixed-wing UAV platform.

---

## 🔬 Candidate Comparison & Selection

Three primary airfoils were analyzed in XFOIL under viscous boundary layer conditions ($N_{\text{crit}} = 9$):

1. **NACA 0012:** Symmetric baseline — predictable, but insufficient lift coefficient ($C_l$) for slow-flight payload efficiency.
2. **Selig S1223:** High-camber cargo profile — excellent maximum $C_l$, but high pitching moment ($C_{m,0} < -0.15$) and severe early separation bubbles at low $Re$.
3. **NACA 4412:** Moderate camber (4%), 12% thickness — optimal trade-off offering gentle stall characteristics, low pitching moment, and high $C_l / C_d$ efficiency.

---

## 📈 XFOIL Polar Analysis Data ($Re = 150,000$)

| Airfoil | $C_{l, \max}$ | Stall Angle ($\alpha_{\text{stall}}$) | Minimum $C_d$ | $(C_l / C_d)_{\max}$ | Pitching Moment ($C_{m,0}$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **NACA 0012** | $1.05$ | $11.0^\circ$ | $0.0092$ | $42.1$ | $0.000$ |
| **Selig S1223** | $1.72$ | $13.5^\circ$ | $0.0185$ | $58.4$ | $-0.162$ |
| **NACA 4412 (Selected)** | **$1.41$** | **$12.5^\circ$** | **$0.0108$** | **$64.2$** | **$-0.088$** |

---

## 🔑 Key Takeaways
* **Laminar Separation Bubble (LSB):** At $Re = 150,000$, the NACA 4412 exhibits a localized laminar separation bubble near $x/c \approx 0.45-0.60$ prior to turbulent reattachment.
* **Sectional Selection:** NACA 4412 was selected as the root-to-tip baseline section due to its high glide ratio efficiency and manageable trim penalty.