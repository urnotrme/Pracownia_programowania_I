import csv
with open("students.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for i in csv_reader:
        if int(i[2])<30:
            print(f'{i[0]}\t{i[1]}\t{i[4]}')