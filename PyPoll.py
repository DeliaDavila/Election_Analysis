# Open dependencies
import csv
import os

# Assign a variable for the data to read
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to write results
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

	# Read and analyze the data
	#Set a file reader variable to use CSV reader function
	file_reader = csv.reader(election_data)

	# Print header row only
	headers = next(file_reader)
	print(headers)

# Using with, open the results file and write to it
with open(file_to_save, "w") as txt_file:
	# Write some data to the file.
	txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")

