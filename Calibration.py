import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
# Replace 'file1.csv', etc., with actual file paths
data_files = ['file1.csv', 'file2.csv', 'Macintosh HD\Users\hgallagh\Desktop\Imaging Science\Radiometry\Lab\GRITT-olivine-63umto300um-i30-DN-spectra-136ms.csv', 'file4.csv', 'file5.csv']
data = [pd.read_csv(file) for file in data_files]

# Example structure of one file: ['Wavelength', 'DN', 'ExposureTime']
dnr_data = []

# Convert DNs to DNRs for all datasets
for df in data:
    df['DNR'] = df['DN'] / df['ExposureTime']
    dnr_data.append(df)

# Plot DNR Spectra
plt.figure(figsize=(10, 6))
for i, df in enumerate(dnr_data):
    plt.plot(df['Wavelength'], df['DNR'], label=f'Dataset {i+1}')
plt.xlabel('Wavelength (nm)')
plt.ylabel('DNR')
plt.title('DNR Spectra')
plt.legend()
plt.show()

# Calibrate radiance (Assume calibration factor is given or derived)
calibration_factors = np.random.rand(len(df['Wavelength']))  # Replace with actual factors
radiance_data = []

for df in dnr_data:
    df['Radiance'] = df['DNR'] * calibration_factors
    radiance_data.append(df)

# Plot Radiance Spectra
plt.figure(figsize=(10, 6))
for i, df in enumerate(radiance_data):
    plt.plot(df['Wavelength'], df['Radiance'], label=f'Dataset {i+1}')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Radiance')
plt.title('Calibrated Radiance Spectra')
plt.legend()
plt.show()
