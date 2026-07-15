import os
import matplotlib.pyplot as plt
import pandas as pd

# Get the folder where this script is saved
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute paths to your exact real files
AIRFOIL_FILE = os.path.join(SCRIPT_DIR, "T1_Re0.150_M0.00_N9.0.txt")
WING_FILE = os.path.join(SCRIPT_DIR, "T1-10_0 m_s-VLM1.txt") # <-- Your actual 3D file name!


def parse_xflr5_polar(filepath):
    """Robustly parses XFLR5 text files, stripping meta-headers and returning a clean DataFrame."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Could not find the file: {filepath}")

    data_lines = []
    columns = []
    header_found = False

    with open(filepath, "r") as f:
        for line in f:
            line_str = line.strip()
            if not line_str:
                continue

            # Identify the column header row (contains alpha, CL, CD, etc.)
            if "alpha" in line_str.lower() and not header_found:
                # Store original column names exactly as they are written
                columns = [col.strip() for col in line_str.split()]
                header_found = True
                continue

            # Capture numeric data rows
            if header_found:
                parts = line_str.split()
                # Check if first item is a number (handles decimals and negative signs)
                if parts and (
                    parts[0].replace(".", "", 1).replace("-", "", 1).isdigit()
                ):
                    # Clean out any trailing empty cells or dashes
                    data_lines.append(parts[:len(columns)])

    if not columns or not data_lines:
        raise ValueError(f"Could not parse valid XFLR5 data from {filepath}")

    # Build and clean DataFrame
    df = pd.DataFrame(data_lines, columns=columns)
    return df.apply(pd.to_numeric, errors="coerce")


if __name__ == "__main__":
    try:
        print(f"Parsing 2D Airfoil polar: {os.path.basename(AIRFOIL_FILE)}...")
        airfoil_df = parse_xflr5_polar(AIRFOIL_FILE)

        print(f"Parsing 3D Wing polar: {os.path.basename(WING_FILE)}...")
        wing_df = parse_xflr5_polar(WING_FILE)

        # Set up a clean, professional aesthetic
        plt.style.use("ggplot")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # --- PLOT 1: 2D Airfoil Efficiency (CL/CD vs alpha) ---
        # Using exact column headers from your raw output
        airfoil_cl_cd = airfoil_df["CL"] / airfoil_df["CD"]
        
        ax1.plot(
            airfoil_df["alpha"],
            airfoil_cl_cd,
            color="royalblue",
            linewidth=2.5,
            marker="o",
            markersize=3,
            label="NACA 4412 (Re=150k)",
        )
        ax1.set_title("2D Airfoil Efficiency Profile", fontsize=12, fontweight="bold")
        ax1.set_xlabel("Angle of Attack, alpha (deg)", fontsize=11)
        ax1.set_ylabel("Lift-to-Drag Ratio (Cl/Cd)", fontsize=11)
        ax1.legend(loc="upper left")
        ax1.grid(True, linestyle="--", alpha=0.5)

        # --- PLOT 2: 3D Wing Performance (CL/CD vs alpha) ---
        # Map to the 3D files' exact uppercase headers
        wing_cl_cd = wing_df["CL"] / wing_df["CD"]
        
        ax2.plot(
            wing_df["alpha"],
            wing_cl_cd,
            color="forestgreen",
            linewidth=2.5,
            marker="s",
            markersize=3,
            label="3D Wing Model (VLM)",
        )
        ax2.set_title("3D Wing Performance Profile", fontsize=12, fontweight="bold")
        ax2.set_xlabel("Angle of Attack, alpha (deg)", fontsize=11)
        ax2.set_ylabel("Glide Ratio (CL/CD)", fontsize=11)
        ax2.legend(loc="upper left")
        ax2.grid(True, linestyle="--", alpha=0.5)

        # Save and show
        plt.tight_layout()
        output_path = os.path.join(SCRIPT_DIR, "aerodynamic_performance_real.png")
        plt.savefig(output_path, dpi=300)
        print(f"\n🎉 Success! Real aerodynamic plot saved to:\n   {output_path}")
        plt.show()

    except Exception as e:
        print(f"\n❌ ERROR RUNNING SCRIPT: {e}")