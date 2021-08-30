import csv
p=set()
x=[]
with open('../Bio_Yodie/Keywords/Sign_or_Symptom.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x.append(row)
print(x)
y=[]
y_new=[]
vocab=set()
y.append(x[0])
y_new.append(x[0])

for i in x[1:]:
    flag=0
    for j in range(len(y_new)):

        if str(y[j]).startswith(str(i[0])):

            y_new[j][1]=int(y_new[j][1])+ int(i[1])
            y_new[j][2]=int(y_new[j][2])+ int(i[2])

            y_new[j][0]+=str("_"+str(y[j])) 
            flag=1
            print(i[0],"XXXXXX")
            break;
        elif str(i[0]).startswith(str(y[j])):
            
            y_new[j][1]=int(y_new[j][1])+ int(i[1])
            y_new[j][2]=int(y_new[j][2])+ int(i[2])

            y_new[j][0]+=str("_"+str(i[0]))
            flag=1
            print(i[0],"XXXXXX")
            break;
    if(flag==0):
        y.append(i[0])
        y_new.append(i)
print(y_new)


with open("merged_symptoms.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(y_new)




