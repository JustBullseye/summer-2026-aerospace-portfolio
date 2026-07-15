import matplotlib.pyplot as plt
import pandas as pd


def load_xflr5_polar(filepath):
    """Parses an XFLR5 exported text polar, skipping the metadata header."""
    # XFLR5 headers typically end and data begins after ~11 lines,
    # but we search for the column names row to be robust.
    skip_rows = 0
    columns = None

    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            if "alpha" in line or "  alpha  " in line:
                skip_rows = i
                columns = [col.strip() for col in line.split() if col.strip()]
                break

    # Read the data, skipping the text header rows
    df = pd.read_csv(
        filepath,
        skiprows=skip_rows + 1,
        delim_whitespace=True,
        names=columns,
        on_bad_lines="skip",
    )
    return df


# 1. Load the exported data files (Update paths as necessary)
try:
    naca_df = load_xflr5_polar("naca4412_2d.txt")
    ag35_df = load_xflr5_polar("ag35_2d.txt")
    wing_df = load_xflr5_polar("wing_3d.txt")
except FileNotFoundError as e:
    print(
        f"Error: {e}. Please ensure your exported .txt files are in the same directory as this script."
    )
    exit()

# Set up clean engineering-style plots
plt.style.use("seaborn-v0_8-whitegrid")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Plot 1: 2D Airfoil Lift-to-Drag Ratio (Cl/Cd vs Alpha) ---
# Check if the file columns use upper or lowercase
naca_cl_cd = naca_df["Cl"] / naca_df["Cd"]
ag35_cl_cd = ag35_df["Cl"] / ag35_df["Cd"]

ax1.plot(
    naca_df["alpha"],
    naca_cl_cd,
    label="NACA 4412 (2D)",
    color="royalblue",
    linewidth=2,
)
ax1.plot(
    ag35_df["alpha"],
    ag35_cl_cd,
    label="Drela AG35 (2D)",
    color="crimson",
    linewidth=2,
)
ax1.set_title("2D Airfoil Efficiency Comparison", fontsize=14, fontweight="bold")
ax1.set_xlabel(r"Angle of Attack, $\alpha$ (deg)", fontsize=12)
ax1.set_ylabel(r"Lift-to-Drag Ratio, $C_l/C_d$", fontsize=12)
ax1.set_xlim([-4, 15])
ax1.legend(frameon=True, fontsize=11)
ax1.grid(True, linestyle="--", alpha=0.6)

# --- Plot 2: 3D Wing Performance (CL/CD vs Alpha) ---
wing_cl_cd = wing_df["CL"] / wing_df["CD"]

ax2.plot(
    wing_df["alpha"],
    wing_cl_cd,
    label="Optimized Tapered Wing (3D)",
    color="forestgreen",
    linewidth=2.5,
)
ax2.set_title("3D Wing Performance Profile", fontsize=14, fontweight="bold")
ax2.set_xlabel(r"Angle of Attack, $\alpha$ (deg)", fontsize=12)
ax2.set_ylabel(r"Glide Ratio, $C_L/C_D$", fontsize=12)
ax2.set_xlim([-4, 15])
ax2.legend(frameon=True, fontsize=11)
ax2.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()

# Save the plot directly to your portfolio assets folder
plt.savefig("wing_performance_comparison.png", dpi=300)
print("Success! Plot saved as 'wing_performance_comparison.png'.")
plt.show()