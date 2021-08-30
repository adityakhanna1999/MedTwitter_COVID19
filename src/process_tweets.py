import json
import numpy
import pickle
import pandas as pf
from extract_tweets import get_tweets
from os import listdir
from os.path import isfile, join


def covid_filtered_tweets(myfile):
    filtered_tweets = []
    # filtered_tweets_mapping=[]
    # filtered_dict={}
    keywords_1 = ["corona", "corona19", "corona2019",
                  "coronaupdate", "coronavirus", "coronavirus19",
                  "coronavirus2019", "coronavirusoutbreak", "coronaviruspandemic",
                  "coronavirustruth", "covid", "covid-19", "covid-19-uk",
                  "covid19", "covid19uk", "covid2019", "covid2019uk",
                  "covid_19", "covid_19_uk", "covid_2019_uk",
                  "coviduk", "covidー19", "sarscov2"]
    # keywords=["#corona","#corona19","#corona2019","#coronaupdate","#coronavirus","#coronavirus19","#coronavirus2019","#coronavirusoutbreak","#coronaviruspandemic","#coronavirustruth","#covid","#covid-19","#covid-19-uk","#covid19","#covid19uk","#covid2019","#covid2019uk","#covid_19","#covid_19_uk","#covid_2019_uk","#coviduk","#covidー19","#sarscov2"]
    # keywords_new=["#coronasymptoms","#covid19symptoms","#covidsymptoms","#hydroxichloroquine","#hydroxychloroquine","#mildsymptoms"]

    texts, timestamps, ids = get_tweets(myfile)
    for i in range(len(texts)):
        texts[i] = texts[i].lower()
        for j in keywords_1:
            if j in texts[i]:
                tweet = {'tweet_id': ids[i],
                         'timestamp': timestamps[i],
                         'text': texts[i]}
                filtered_tweets.append(tweet)
                # filtered_tweets.append(texts[i])
                # filtered_tweets_mapping.append(timestamps[i])
                break
    return filtered_tweets


mypath = "../Data/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

tweets = []
count = 1
for filename in onlyfiles:
    print(filename)
    date = filename[20:30]  # TODO - extract date from tweet itself rather than filename
    if "covid" in filename:
        # j=filename[:-5]
        filtered_tweets = covid_filtered_tweets(mypath + filename)
        # print(filtered_tweets)
        for i in range(len(filtered_tweets)):
            tweet = filtered_tweets[i].copy()
            tweet['id'] = count
            tweet['date'] = str(date)
            tweets.append(tweet)
            # tweet_dict[str(count)+"_"+str(x)+"_"+str(filtered_tweets_mapping[i])]=filtered_tweets[i]
            count += 1

with open("../Tweets/Extracted.txt", 'w') as f:
    json.dump(tweets, f)
