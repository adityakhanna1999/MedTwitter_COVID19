import json, csv
from utils import remove_garbage
import datetime

f1 = open("../Bio_Yodie/Keywords/merged_symptoms.csv", "r")
final_f = open("../Bio_Yodie/Keywords/final_symtoms.csv", "w")
f2 = open("../Bio_Yodie/symptoms_tweets.txt", "w")
with open('../Bio_Yodie/Keywords/keywords_larger_data.json', 'r') as f:
    entities = json.load(f)

f = open("../Tweets/Extracted.txt", "r")
tweets = json.load(f)
csv_writer = csv.writer(final_f)
csv_writer.writerow(["Keyword", "Engagements", "Tweets(unique)", "First occurance"])
csv_reader = csv.reader(f1)
symptoms = entities[5]['keywords']
first = 1
for row in csv_reader:
    if first:
        first = 0
        continue
    keyw = row[0]
    # print(keyw)
    keyws = keyw.split('_')
    inds = []
    for keyword in keyws:
        for i in range(len(symptoms)):
            if symptoms[i]['name'] == keyword:
                inds.append(i)
                break
    counts = [symptoms[i]['count'] for i in inds]
    counts = [len(key) for key in keyws]
    print(counts)
    maxi = -1
    max_ind = 0
    for i in range(len(counts)):
        if counts[i] > maxi:
            maxi = counts[i]
            max_ind = i
    name = symptoms[inds[max_ind]]['name']
    print(name)
    tweet_ids = []
    for ind in inds:
        tweet_ids += symptoms[ind]['ids']
    tweet_ids = list(set(tweet_ids))

    if '/' in name:
    # TODO hardcoded
            name = "nausea-vomiting"
    fl = open("../Bio_Yodie/Tweets/Sign_or_Symptom_merged/" + name + ".txt", "w")
    # id_list = symptom['ids']
    tweet_texts = []
    tweet_timestamps = []
    for tweet in tweets:
        if tweet['id'] in tweet_ids:
            tweet_texts.append(tweet['text'])
            tweet_timestamps.append(int(tweet['timestamp']))
    min_timestamp = min(tweet_timestamps)
    timestamp = datetime.datetime.fromtimestamp(min_timestamp//1000)
    date = timestamp.strftime('%Y-%m-%d')

    tweet_texts = list(map(remove_garbage, tweet_texts))
    tweet_texts = list(set(tweet_texts))
    unique = len(tweet_texts)
    engage = len(tweet_ids)
    csv_writer.writerow([name, engage, unique, date])

    for text in tweet_texts:

        fl.write(text)
        fl.write('\n\n-----------\n\n')


# for symptom in symptoms:
#     keyword = symptom['name']
#     print(keyword)
#     if '/' in keyword:
#         # TODO hardcoded
#         keyword = "nausea-vomiting"
#     fl = open("../Bio_Yodie/Tweets/Sign_or_Symptom/"+keyword+".txt", "w")
#     id_list = symptom['ids']
#     tweet_texts = []
#     for tweet in tweets:
#         if tweet['id'] in id_list:
#             tweet_texts.append(tweet['text'])
#
#     # tweet_texts = list(map(deEmojify, tweet_texts))
#     tweet_texts = list(map(remove_garbage, tweet_texts))
#     tweet_texts = list(set(tweet_texts))
#     # f2.write("==========\n")
#     # f2.write(keyword + '\n')
#     # f2.write("==========\n\n")
#     for text in tweet_texts:
#         # text = " ".join(tweet_texts[i])
#         # text = tweet_texts[i]
#         fl.write(text)
#         fl.write('\n\n-----------\n\n')