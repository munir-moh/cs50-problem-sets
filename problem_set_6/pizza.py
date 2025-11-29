import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit()

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit()

if not os.path.isfile(filename):
    sys.exit()

table = []

with open(filename, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        table.append(row)

print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
