import PyPDF2 as pdf
from tika import parser
import requests
from requests.auth import HTTPBasicAuth
import json
import os
import tqdm
import csv
from utils import remove_garbage

url = "https://cloud-api.gate.ac.uk/process-document/bio-yodie"
# user = 'gc3qjmss75en'
user = 'gcga3jmwd2ca'
# password = 'c15rnw5oxeqivf9t15fd'
password = 'og9donz4tqnx9j1jpan4'
headers = {'Content-type': 'text/plain'}
annotations = ["Bio:Drug", "Bio:Disease", "Bio:Sign_or_Symptom",
               "Bio:Clinical_Drug", "Bio:Pharmacologic_Substance", "Bio:Antibiotic"]

url += "?"
for i in annotations:
    url += ("annotations=" + i + "&")
url = url[:-1]

dir_path = '../Pre-prints/Pdf'
keywords = {}
for file in tqdm.tqdm(os.listdir(dir_path)):
    # print(file)
    if file[-4:-1] != ".pd":
        continue
    raw = parser.from_file(dir_path + '/' + file)
    text = raw['content']
    # pdf_file = open(dir_path + '/' + file, 'rb')
    # pdf_reader = pdf.PdfFileReader(pdf_file)
    # if pdf_reader.isEncrypted:
    #     print(file, "encrypted")
    #     exit(0)
    # text = ""
    #
    # for i in range(pdf_reader.numPages):
    #     pdf_page = pdf_reader.getPage(i)
    #     page_text = pdf_page.extractText()
    #     # if i == 1:
    #     #     print(page_text)
    #     text += page_text

    # Replace new line with space
    text = text.replace('\n', '')
    text = text.lower()
    # print(text)
    text = remove_garbage(text)
    text = " ".join(text.split()[0:7000])
    tf = open('../Pre-prints/Text' + '/' + file[0:-4] + '.txt', 'w')
    tf.write(text)
    # print(file, "Length: ", len(text))
    # continue
    response = requests.post(url,
                             auth=HTTPBasicAuth(user, password),
                             headers=headers,
                             data=text)

    response = response.json()
    f = open('../Pre-prints/JSON_responses' + '/' + file[0:-4] + '.json', 'w')
    json.dump(response, f)

    try:
        entities = response['entities']
    except KeyError as e:
        print("Failed", response, e)
        exit(0)

    for entity in entities:
        res_keywords = entities[entity]
        i = 0
        for keyword in res_keywords:

            if 'string_orig' in keyword.keys():
                keyword_text = keyword['string_orig']
            elif '_string' in keyword.keys():
                keyword_text = keyword['_string']
            else:
                print("Unknown type")
                continue
            if entity in keywords:
                keywords[entity].add(keyword_text)
            else:
                keywords[entity] = set()
        # print(entity, keyword_text)
    # print(response)
# print(keywords)

for entity in keywords:
    f = open('../Pre-prints/Keywords/' + entity + '.csv', 'w')
    writer = csv.writer(f)
    for k in keywords[entity]:
        writer.writerow([k])
#SSRN-id3561560.pdf