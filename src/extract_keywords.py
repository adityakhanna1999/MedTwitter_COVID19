import json
import requests
from utils import get_start_indices, divide_in_chunks
from tqdm import tqdm

from requests.auth import HTTPBasicAuth

url = "https://cloud-api.gate.ac.uk/process-document/bio-yodie"
# user = 'gc3qjmss75en'
user = 'gcga3jmwd2ca'
# password = 'c15rnw5oxeqivf9t15fd'
password = 'og9donz4tqnx9j1jpan4'
headers = {'Content-type': 'text/plain'}
annotations = ["Bio:Drug", "Bio:Disease", "Bio:Anatomy", "Bio:Care", "Bio:Observation", "Bio:Sign_or_Symptom",
               "Bio:Clinical_Drug", "Bio:Pharmacologic_Substance", "Bio:Antibiotic", "Bio:Investigation"]

url += "?"
for i in annotations:
    url += ("annotations=" + i + "&")
url = url[:-1]
print(url)

with open("../Tweets/clean_tweets.json", 'r') as f:
    tweets = json.load(f)

text_list = [tweet['text'] for tweet in tweets]

CHUNK_SIZE = 130
start_index = get_start_indices(text_list)
words_list = divide_in_chunks(text_list, CHUNK_SIZE)

lens = [len(data) for data in words_list]
max_len = max(lens)
max_ind = lens.index(max_len)
print("Maximum length of a chunk:", max_len, max_ind)

keywords = {}
for q in tqdm(range(len(words_list))):
    # if q != max_ind:
    #     continue
    data = words_list[q]
    response = requests.post(url,
                             auth=HTTPBasicAuth(user, password),
                             headers=headers,
                             data=data)
    response = response.json()
    with open('../Bio_Yodie/JSON_response/json_response_new' + '_' + str(q), 'w') as outfile:
        json.dump(response, outfile)
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

            start = keyword['indices'][0]

            id = CHUNK_SIZE * q
            offset = start_index[id]
            while id < min(CHUNK_SIZE * (q + 1), len(start_index)):
                if start < start_index[id] - offset:
                    break
                id += 1

            if entity in keywords.keys():
                if keyword_text in keywords[entity].keys():
                    keywords[entity][keyword_text].append(id)
                else:
                    keywords[entity][keyword_text] = [id]
            else:
                keywords[entity] = {keyword_text: [id]}

# Convert keywords into JSON format
keywords_json = []

for entity in keywords.keys():
    temp_keywords_dict = keywords[entity]
    temp_keywords = []
    for name in temp_keywords_dict.keys():
        ids = temp_keywords_dict[name]
        ids = sorted(list(set(ids)))  # Removed duplicates
        temp = {'name': name,
                'count': len(ids),
                'ids': ids}
        temp_keywords.append(temp)
    keywords_json.append({
        'entity': entity,
        'keywords': temp_keywords
    })

with open("../Bio_Yodie/Keywords/keywords_larger_data.json", "w") as outer:
    json.dump(keywords_json, outer)
