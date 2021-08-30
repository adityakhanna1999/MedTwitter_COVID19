import csv

f = open('../Bio_Yodie/Tweets/Sign_or_Symptom/CSV/chill.csv', 'r')

reader = csv.reader(f, delimiter='&')

for r in reader:
    print(r)
