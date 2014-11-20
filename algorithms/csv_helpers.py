__author__ = 'timothyahong'
import csv


def array_to_csv(filename, header_row, rows):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header_row)
        for row in rows:
            writer.writerow(row)
