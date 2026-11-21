import csv

# Read the orders CSV file
with open("data/orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
