import numpy as np

# --- 1. OPERATING FLUID CONDITIONS ---
V = 10.0          # Cruise velocity (m/s)
nu = 1.5e-5       # Kinematic viscosity of air (m^2/s)
rho = 1.225       # Density of air (kg/m^3)
S_ref = 0.40      # Wing reference area (m^2)

def skin_friction_cf(reynolds_number):
    """Flat plate turbulent skin friction coefficient (Prandtl-Schlichting)."""
    return 0.074 / (reynolds_number ** 0.2)

# --- 2. FUSELAGE COMPONENT ---
L_fuse = 0.90     # Length (m)
d_fuse = 0.06     # Max equivalent diameter (m)
S_wet_fuse = np.pi * d_fuse * L_fuse * 0.75  # Approx wetted area (m^2)

Re_fuse = (V * L_fuse) / nu
Cf_fuse = skin_friction_cf(Re_fuse)

finess_ratio = L_fuse / d_fuse
FF_fuse = 1 + (60 / (finess_ratio**3)) + (finess_ratio / 400)
Q_fuse = 1.0  # Isolated body interference factor

CD0_fuse = (Cf_fuse * FF_fuse * Q_fuse * S_wet_fuse) / S_ref

# --- 3. TAIL SURFACES (HORIZONTAL + VERTICAL) ---
S_wet_tail = 0.0936   # Total wetted area of tailplane (m^2)
MAC_tail = 0.09       # Mean aerodynamic chord of tail (m)
tc_ratio_tail = 0.09  # NACA 0009 thickness ratio (9%)

Re_tail = (V * MAC_tail) / nu
Cf_tail = skin_friction_cf(Re_tail)

FF_tail = 1 + 2 * tc_ratio_tail + 100 * (tc_ratio_tail**4)
Q_tail = 1.05  # Tail-fuselage junction interference factor

CD0_tail = (Cf_tail * FF_tail * Q_tail * S_wet_tail) / S_ref

# --- 4. WING PROFILE DRAG (FROM WEEK 4 PARSED POLAR) ---
# Baseline profile drag coefficient for NACA 4412 at alpha ~ 0 deg
CD0_wing = 0.0062  

# --- 5. TOTAL AIRCRAFT CD0 BUILD-UP ---
CD0_total = CD0_wing + CD0_fuse + CD0_tail

print("==================================================")
print("     EMPIRICAL PARASITIC DRAG BUILD-UP RESULTS    ")
print("==================================================")
print(f"Wing Profile CD0:       {CD0_wing:.5f}")
print(f"Fuselage Parasite CD0:  {CD0_fuse:.5f}")
print(f"Tailplane Parasite CD0: {CD0_tail:.5f}")
print("--------------------------------------------------")
print(f"TOTAL AIRCRAFT CD0:     {CD0_total:.5f}")
print("==================================================")