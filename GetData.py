###This is the first part of the Radiometry lab for 2025, we are attempting to find a linear regression to take this file,
#with digital numbers uncalibrated DNs to be compatible with the calibrated Helios Sphere readings of these
# same five light levels.


import csv

# Open the CSV file in read mode ('r')
# 'newline=''' is important to prevent extra blank rows when reading
with open('/Users/hgallagh/Desktop/Imaging_Science/Rad_Lab_2025/ASD-DN-spectra 1(Sheet1).csv', mode='r', newline='') as csv_file:
    # Create a csv.reader object
    csv_reader = csv.reader(csv_file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        print(row)