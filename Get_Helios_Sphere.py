###This is the first part of the lab this is the calibrated radiance files given from the
# Helios Integrating Sphere with five different light levels.

import csv

# Open the CSV file in read mode ('r')
# 'newline=''' is important to prevent extra blank rows when reading
with open('/Users/hgallagh/Desktop/Imaging_Science/Rad_Lab_2025/sphere-radiance-spectra-interp-corr 1(Sheet1).csv', mode='r', newline='') as csv_file:
    # Create a csv.reader object
    csv_reader = csv.reader(csv_file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        print(row)