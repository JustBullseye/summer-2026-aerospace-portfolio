import os
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'figure.titlesize': 14
})

# --- 1. PATH B: EMPIRICAL COMPONENT BUILD-UP (RAYMER / HOERNER) ---
V = 10.0          # Cruise speed (m/s)
nu = 1.5e-5       # Kinematic viscosity (m^2/s)
S_ref = 0.29      # Reference Wing Area (m^2)
c_mac = 0.145     # Mean Aerodynamic Chord (m)

# Wing Parasite Drag Component
S_wet_wing = 2 * S_ref
Re_wing = (V * c_mac) / nu
Cf_wing = 0.074 / (Re_wing ** 0.2)
FF_wing = 1 + 2*(0.12) + 100*(0.12**4)  # NACA 4412 (12% thickness)
Q_wing = 1.0  # Interference factor
CD0_wing = (Cf_wing * FF_wing * Q_wing * S_wet_wing) / S_ref

# Fuselage Parasite Drag Component
L_fuse, d_fuse = 0.90, 0.08
S_wet_fuse = np.pi * d_fuse * L_fuse * 0.75
Re_fuse = (V * L_fuse) / nu
Cf_fuse = 0.074 / (Re_fuse ** 0.2)
finesse = L_fuse / d_fuse
FF_fuse = 1 + (60 / (finesse**3)) + (finesse / 400)
Q_fuse = 1.0
CD0_fuse = (Cf_fuse * FF_fuse * Q_fuse * S_wet_fuse) / S_ref

# Tail Parasite Drag Component
S_wet_tail = 0.08
Re_tail = (V * 0.09) / nu
Cf_tail = 0.074 / (Re_tail ** 0.2)
FF_tail = 1 + 2*(0.09) + 100*(0.09**4)
Q_tail = 1.05
CD0_tail = (Cf_tail * FF_tail * Q_tail * S_wet_tail) / S_ref

# Miscellaneous/Excrescence Drag (5% allowance)
CD0_parasitic_total = (CD0_wing + CD0_fuse + CD0_tail) * 1.05

print("==================================================")
print("     PATH B: REVISED EMPIRICAL BUILD-UP           ")
print("==================================================")
print(f"Wing Parasite CD0:     {CD0_wing:.5f}")
print(f"Fuselage Parasite CD0: {CD0_fuse:.5f}")
print(f"Tail Parasite CD0:     {CD0_tail:.5f}")
print("--------------------------------------------------")
print(f"TOTAL PARASITIC CD0:   {CD0_parasitic_total:.5f}\n")

# --- 2. PATH A: PARSE XFLR5 3D POLAR DATA ---
script_dir = os.path.dirname(os.path.abspath(__file__))

candidate_paths = [
    os.path.join(script_dir, "polars", "full_aircraft_3d.txt"),
    os.path.join(script_dir, "full_aircraft_3d.txt"),
    os.path.join(os.getcwd(), "polars", "full_aircraft_3d.txt"),
    os.path.join(os.getcwd(), "full_aircraft_3d.txt")
]

polar_path = None
for path in candidate_paths:
    if os.path.exists(path):
        polar_path = path
        break

alpha_xflr, CL_xflr, CD_xflr, L_D_xflr = [], [], [], []

if polar_path:
    print(f"[INFO] Parsing XFLR5 polar file: {polar_path}")
    with open(polar_path, 'r') as f:
        lines = f.readlines()
    
    start_reading = False
    for line in lines:
        if "alpha" in line and "CL" in line and "CD" in line:
            start_reading = True
            continue
        if start_reading and line.strip():
            parts = line.split()
            if len(parts) >= 6:
                try:
                    a = float(parts[0])
                    cl = float(parts[2])
                    cd = float(parts[5])
                    
                    alpha_xflr.append(a)
                    CL_xflr.append(cl)
                    CD_xflr.append(cd)
                    L_D_xflr.append(cl / cd if cd > 0 else 0)
                except ValueError:
                    continue

alpha_xflr = np.array(alpha_xflr)
CL_xflr = np.array(CL_xflr)
CD_xflr = np.array(CD_xflr)
L_D_xflr = np.array(L_D_xflr)

# --- 3. GENERATE COMPARISON PLOTS ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

if len(CD_xflr) > 0:
    ax1.plot(CD_xflr, CL_xflr, 'o-', color='#2b5c8f', lw=2.5, label='Path A: XFLR5 3D Panel')

if len(CL_xflr) > 0:
    AR = 13.8  
    e = 0.78   # Realistic Oswald efficiency for low-Re full body model
    K = 1 / (np.pi * AR * e)
    CD_empirical = CD0_parasitic_total + K * (CL_xflr**2)
    ax1.plot(CD_empirical, CL_xflr, '--', color='#d95f02', lw=2.5, label='Path B: Empirical Build-up')

ax1.set_title('Drag Polar Comparison ($C_L$ vs $C_D$)', fontweight='bold')
ax1.set_xlabel('Total Drag Coefficient ($C_D$)')
ax1.set_ylabel('Lift Coefficient ($C_L$)')
if len(CD_xflr) > 0 or len(CL_xflr) > 0:
    ax1.legend(frameon=True)
ax1.grid(True, linestyle='--', alpha=0.6)

if len(L_D_xflr) > 0:
    ax2.plot(alpha_xflr, L_D_xflr, 's-', color='#2ca02c', lw=2.5, label='Full Aircraft ($C_L/C_D$)')
    
    LD_empirical = CL_xflr / CD_empirical
    ax2.plot(alpha_xflr, LD_empirical, '--', color='#d95f02', lw=2.5, label='Empirical Model ($C_L/C_D$)')

ax2.set_title('Full Aircraft Glide Ratio Profile', fontweight='bold')
ax2.set_xlabel('Angle of Attack, $\\alpha$ (deg)')
ax2.set_ylabel('Glide Ratio ($C_L / C_D$)')
if len(L_D_xflr) > 0:
    ax2.legend(frameon=True)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

output_img = os.path.join(script_dir, "week5_parasitic_drag_comparison.png")
plt.savefig(output_img, dpi=300)
print(f"\n[SUCCESS] Updated comparison plot saved to: {output_img}")
plt.show()