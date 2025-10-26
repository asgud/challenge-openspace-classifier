import csv
from utils.openspace import Openspace     # This line imports your Openspace class from your file openspace.py


# --- Step 1: Read names from new_colleagues.csv ---
names = []

# Open the CSV file in read mode
with open("new_colleagues.csv", "r") as file:
    reader = csv.reader(file)  # simple reader for files without headers
    for row in reader:
        if not row:  # skip empty lines
            continue
        # Take only the first column (name)
        name = row[0].strip()              # strip() will remove empty spaces in back and front of name
        if name:  # make sure it's not empty
            names.append(name)

# --- Step 2: Create the openspace ---
NUMBER_OF_TABLES = 6     # you can change this
TABLE_CAPACITY = 4        # seats per table
O1 = Openspace(NUMBER_OF_TABLES, TABLE_CAPACITY)

# --- Step 3: Randomly assign names to seats ---
O1.organize(names)

# --- Step 4: Display and save the seating plan ---
O1.display()
O1.store("seating_plan.txt")
