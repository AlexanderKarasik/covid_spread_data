import csv
list = []

# Open the CSV file for reading and store a reference
# to the opened file in a variable named csv_file.
with open("us_vacs.csv", "rt") as csv_file:

    # Use the csv module to create a reader object
    # that will read from the opened CSV file.
    reader = csv.reader(csv_file)
    
    # The first line of the CSV file contains column
    # headings and not information, so this statement
    # skips the first line of the CSV file.
    next(reader)
    
    # Read the rows in the CSV file one row at a time.
    # The reader object returns each row as a list.
    for row in reader:
        
        list.append(row)
for i in list:
    variable = i[4]
    variable1 = variable[:-2]
    if not variable1.isdigit():
        variable1 = 1
        float(variable1)
   # variable.strip( )
   # variable1 = float(variable)
    print(f"Variable is{variable1}end")