import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

input_file, output_file = sys.argv[1], sys.argv[2]

try:
    with open(input_file, newline="") as infile:
        reader = csv.DictReader(infile)
        cleaned = []
        for row in reader:
            last, first = row["name"].split(", ")
            cleaned.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

with open(output_file, "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(cleaned)

