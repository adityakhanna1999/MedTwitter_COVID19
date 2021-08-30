import os
import csv

dir_path = "../Bio_Yodie/Tweets/Sign_or_Symptom/CSV"
flist = os.listdir(dir_path)

c00 = 0
c01 = 0
c10 = 0
c11 = 0
cu = 0
lc = 0

for f in flist:

    file = open(dir_path + "/" + f, "r")
    reader = csv.reader(file, delimiter='&')
    i = 0
    for row in reader:
        if i == 0:
            i = 1
            continue
        if f[0] <= 'c':
            lc += 1
        if int(row[2]) == 0 and int(row[3]) == 1:
            c01 += 1
        elif int(row[2]) == 1 and int(row[3]) == 1:
            c11 += 1
        elif int(row[2]) == 0 and int(row[3]) == 0:
            c00 += 1
        elif int(row[2]) == 1 and int(row[3]) == 0:
            c10 += 1
        else:
            cu += 1

print(c00, c10, c01, c11, cu, lc)

