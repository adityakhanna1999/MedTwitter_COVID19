import json
import csv

f = open('../Bio_Yodie/Keywords/keywords_larger_data.json', 'r')
kws = json.load(f)

disease = kws[1]['keywords']
disease_names = [k['name'] for k in disease]

sympts = kws[5]['keywords']
sympts_names = [k['name'] for k in sympts]

exclusive_dis = []
for dis in disease_names:
    if dis not in sympts_names:
        exclusive_dis.append(dis)
f1 = open('../Bio_Yodie/Keywords/exclusive_disease.csv', 'w')
writer = csv.writer(f1)
writer.writerows([[i] for i in exclusive_dis])
print(len(disease_names), len(exclusive_dis), len(sympts_names))