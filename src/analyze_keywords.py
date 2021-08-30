import json
import csv
from utils import remove_garbage

# with open('../Bio_Yodie/Keywords/keywords_larger_data.json', 'r') as f:
#     entities = json.load(f)
#
# f = open("../Tweets/clean_tweets.json", "r")
# tweets = json.load(f)
# # print(entities[0])
#
# for i in range(len(entities)):
#     entity = entities[i]['entity']
#     keywords = entities[i]['keywords']
#     header = ["Keyword", "Engagements", "Tweets(unique)"]
#     content = []
#     print(entity)
#     for keyword_obj in keywords:
#
#         id_list = keyword_obj['ids']
#         tweet_texts = []
#         for tweet in tweets:
#             if tweet['id'] in id_list:
#                 tweet_texts.append(tweet['text'])
#
#         unique_count = len(list(set(tweet_texts)))
#         content.append([keyword_obj['name'], keyword_obj['count'], unique_count])
#
#     with open('../Bio_Yodie/Keywords/' + entity + '.csv', 'w') as f:
#         csv_writer = csv.writer(f)
#         content = sorted(content, key=lambda x: x[1], reverse=True)
#         csv_writer.writerow(header)
#         csv_writer.writerows(content)
#
# print("done")
# exit(0)

###################################
# def remove_garbage(word_list):
#     output_list = [i for i in word_list if '@' not in i and '&amp' not in i and "https://" not in i]
#     return output_list
# def deEmojify(inputString):
#     return inputString.encode('ascii', 'ignore').decode('ascii')
#
# def remove_username(inputString):
#     words = inputString.split()
#     output_list = [i for i in words if '@' not in i and '&amp' not in i and "https://" not in i]
#     output = " ".join(output_list)
#     return output

f1 = open("../Bio_Yodie/Keywords/Sign_or_Symptom.csv", "r")
f2 = open("../Bio_Yodie/symptoms_tweets.txt", "w")
with open('../Bio_Yodie/Keywords/keywords_larger_data.json', 'r') as f:
    entities = json.load(f)

f = open("../Tweets/Extracted.txt", "r")
tweets = json.load(f)

symptoms = entities[5]['keywords']
for symptom in symptoms:
    keyword = symptom['name']
    print(keyword)
    if '/' in keyword:
        # TODO hardcoded
        keyword = "nausea-vomiting"
    fl = open("../Bio_Yodie/Tweets/Sign_or_Symptom/Text/"+keyword+".txt", "w")
    fl2 = open("../Bio_Yodie/Tweets/Sign_or_Symptom/CSV/"+keyword+".csv", "w")
    id_list = symptom['ids']
    tweet_texts = []
    tweet_ids = []
    text_to_id = {}
    for tweet in tweets:
        if tweet['id'] in id_list:
            tweet_texts.append(tweet['text'])
            tweet_ids.append(tweet['id'])
            # text_to_id[tweet['text']] = tweet['id']

    # tweet_texts = list(map(deEmojify, tweet_texts))
    tweet_texts = list(map(remove_garbage, tweet_texts))
    for i in range(len(tweet_texts)):
        text_to_id[tweet_texts[i]] = tweet_ids[i]
    # for text in tweet_texts:
    #     text_to_id[text]
    tweet_texts = list(set(tweet_texts))
    # f2.write("==========\n")
    # f2.write(keyword + '\n')
    # f2.write("==========\n\n")
    for text in tweet_texts:
        # text = " ".join(tweet_texts[i])
        # text = tweet_texts[i]
        fl.write(text)
        fl.write('\n\n-----------\n\n')
    writer = csv.writer(fl2, delimiter='&')
    writer.writerow(['id', 'text', 'COVID relevance', 'BioYodie relevance'])
    for text in tweet_texts:
        # text = " ".join(tweet_texts[i])
        # text = tweet_texts[i]
        writer.writerow([text_to_id[text], text, 2, 2])
        # fl2.write(text)
        # fl2.write('\n')



# reader = csv.reader(f1)

# i = 0
# for row in reader:
#     if i == 0:
#         i = 1
#         continue
#     keyword =
#     print(row)


#
#

#
#
# for i in range(len(tweets)):
#     for j in range(len(tweets)):
#         if tweets[i]['text'] == tweets[j]['text'] and i != j:
#             print(tweets[i]['tweet_id'], tweets[j]['tweet_id'])
#             exit(0)
# tweet_texts = list(set([tweet['text'] for tweet in tweets]))
# tweet_texts = [text.split() for text in tweet_texts]
# tweet_texts = list(set([" ".join(remove_garbage(i)) for i in tweet_texts]))

# print(len(tweet_texts))


#
# for line in f1:
#     if len(line) < 2:
#         continue
#     keyword = line.split()[:-1]
#     keyword = " ".join(keyword)
#     print(keyword)
#     f2.write("==========\n")
#     f2.write(keyword + '\n')
#     f2.write("==========\n\n")
#     for i in range(len(tweet_texts)):
#         if keyword in tweet_texts[i]:
#             # text = " ".join(tweet_texts[i])
#             text = tweet_texts[i]
#             f2.write(text)
#             f2.write('\n-----------\n')

