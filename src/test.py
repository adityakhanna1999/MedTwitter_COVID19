import json
import pandas as pd
import requests
from os import listdir
import pickle
from os.path import isfile, join
from flatten_json import flatten 


from requests.auth import HTTPBasicAuth 
url="https://cloud-api.gate.ac.uk/process-document/bio-yodie"
user = 'gc3qjmss75en'
password = 'c15rnw5oxeqivf9t15fd'
headers = {'Content-type': 'text/plain'}
#annotations=["Bio:Drug","Bio:Disease","Bio:Observation","Bio:Sign_or_Symptom","Bio:Clinical_Drug","Bio:Pharmacologic_Substance","Bio:Antibiotic","Bio:Investigation"]


#### Annotations######
######################


def deEmojify(inputString):
	return inputString.encode('ascii', 'ignore').decode('ascii')



month="04"
year="2020"
day="28"
serial="001"
annotations=["Bio:Drug","Bio:Disease","Bio:Anatomy","Bio:Care","Bio:Observation","Bio:Sign_or_Symptom","Bio:Clinical_Drug","Bio:Pharmacologic_Substance","Bio:Antibiotic","Bio:Investigation"]


#### Annotations######
url=url+"?"
for i in annotations:
	url=url+"annotations="+i+"&"
url=url[:-1]
print(url)


myfile2="covid-cardio-tweets-"+year+"-"+month+"-"+day+"-"+serial+".txt"

pa=" diabetes, sugar covid"

i=myfile2
if "covid" in i:
	with open ("../Tweets/Extracted_"+i, 'r') as f:
		p=f.read()
		print(len(p))
		p=deEmojify(p)
		keywords=[]
		response = requests.post(url,auth = HTTPBasicAuth(user, password),headers= headers,data=pa)
		response=response.json()
		print(response)
		flat_json = flatten(response) 

		for j in flat_json:
			if "string_orig" in j:
				keywords.append(flat_json[j])
		print(keywords)

# for i in range(len(response)):
# 	print(response[i]
