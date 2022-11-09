import csv
import os

set_header = input("Set header?[y]/n >> ")
if not set_header or set_header == "y":
    c = int(input("The number of columns: "))
    header = []
    for i in range(c):
        cname = input("column:{} >> ".format(i))
        header.append(cname)

path = input("Path: ")
for file in os.listdir(path):
    base, ext = os.path.splitext(file)

    if ext == ".txt":
        with open(path + "/" + file, "r") as ftxt, open(
            path + "/" + base + ".csv", "x", newline=""
        ) as fcsv:
            reader = csv.reader(ftxt, delimiter=" ", skipinitialspace=True)
            writer = csv.writer(fcsv)
            writer.writerow(header)
            writer.writerows(reader)
