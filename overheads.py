from pathlib import Path
import csv

def identify_overheads(file_path):
    """
    Reads the CSV file containing overheads data and identifies the highest overhead category.
    Returns the string representation of the highest overhead.
    """
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        overheads = {}

        for row in reader:
            category = row[0]
            amount = float(row[1])
            overheads[category] = amount

        largest_overhead = max(overheads, key=overheads.get)
        return f"[HIGHEST OVERHEAD] {largest_overhead}: {overheads[largest_overhead]}%\n"