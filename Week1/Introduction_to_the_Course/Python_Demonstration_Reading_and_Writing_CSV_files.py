# Data Files and Summary statistics
import csv

with open("csv_files/mpg.csv") as csvfile:
    mpg = list(csv.DictReader(csvfile))
    print(mpg[:3])
    print(len(mpg))
    print(mpg[0].keys())


