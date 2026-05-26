import matplotlib.pyplot as plt
import pandas as pd

# List of your exported XFLR5 text files and their display names
airfoils = {
    'NACA 2412': 'naca2412.txt',
    'S1223': 's1223.txt',
    'S7012': 's7012.txt',
    'AG35': 'ag35.txt',
    'NACA 4412': 'naca4412.txt'
}

plt.figure(figsize=(10, 6))

for name, filename in airfoils.items():
    # XFLR5 exports have a bunch of header lines. 
    # skiprows=11 or 12 skips the text headers to get straight to the numbers.
    try:
        data = pd.read_csv(filename, skiprows=11, sep=r'\s+', header=None)
        # Column 0 is usually Alpha (angle), Column 1 is Cl (Lift), Column 2 is Cd (Drag)
        alpha = data[0]
        cl = data[1]
        cd = data[2]
        
        # Calculate L/D ratio (Lift divided by Drag)
        ld_ratio = cl / cd
        
        # Plot Angle of Attack vs Lift-to-Drag Ratio
        plt.plot(alpha, ld_ratio, label=f'{name}')
    except Exception as e:
        print(f"Could not read {filename}. Make sure the path is correct! Error: {e}")

plt.title('Airfoil Comparison: Lift-to-Drag Ratio (L/D) at Re=100,000')
plt.xlabel('Angle of Attack (alpha)')
plt.ylabel('Glide Efficiency (L/D)')
plt.grid(True, linestyle='--')
plt.legend()

# Save the plot as an image for your portfolio markdown report
plt.savefig('airfoil_comparison_plot.png', dpi=300)
plt.show()