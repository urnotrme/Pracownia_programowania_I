import csv

with open("people.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    count=0
    for line in csv_reader:
        for i in line:
            if i[-1]=="Female" and i[-2]>160 and i[-2]<180:
                count+=1
    print(count)
                
            
    
#    with open("new.csv", "w") as new_file:
#        csv_writer=csv.writer(new_file, delimiter='-')
    
#        for line in csv_reader:
#           csv_writer.writerow(line)

