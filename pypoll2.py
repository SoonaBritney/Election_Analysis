import os

# Module for reading CSV files
import csv

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Counties in the Election\n")
outfile.write("------------------------\n")
outfile.write("Arapahoe\nDenver\nJefferson\nEl Paso ")

# Close the file
outfile.close()

