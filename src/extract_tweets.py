import json
import numpy
import pandas as pf

def get_tweets(myfile):
	Tweet_List = []
	counter=[]
	final_tweet_texts=[]
	final_tweet_timestamps=[]
	final_tweet_ids=[]
	count=0
	with open(myfile) as f:
		for obj in f:
		    p = json.loads(obj)
		    Tweet_List.append(p)

	for i in range(len(Tweet_List)):
		counter.append(0)
		final_tweet_texts.append("")
		final_tweet_timestamps.append("")
		final_tweet_ids.append("")

	for i in range(len(Tweet_List)):
		concat_tweet=""
		duplicate_text_remover=set()


		if "quoted_status" in Tweet_List[i].keys():
			if'extended_tweet' in Tweet_List[i]["quoted_status"].keys():
				if 'full_text' in Tweet_List[i]["quoted_status"]['extended_tweet'].keys():
					tweet_1=Tweet_List[i]["quoted_status"]['extended_tweet']['full_text']
					duplicate_text_remover.add(tweet_1)
					counter[i]=1
					count+=1

		if "retweeted_status" in Tweet_List[i].keys():
			if'extended_tweet' in Tweet_List[i]["retweeted_status"].keys():
				if 'full_text' in Tweet_List[i]["retweeted_status"]['extended_tweet'].keys():
					tweet_2=Tweet_List[i]["retweeted_status"]['extended_tweet']['full_text']
					duplicate_text_remover.add(tweet_2)
					counter[i]=1
					count+=1

		if "retweeted_status" in Tweet_List[i].keys():
			if'quoted_status' in Tweet_List[i]["retweeted_status"].keys():
				if 'extended_tweet' in Tweet_List[i]["retweeted_status"]["quoted_status"].keys():
					if 'full_text' in Tweet_List[i]["retweeted_status"]["quoted_status"]['extended_tweet'].keys():
						tweet_3=Tweet_List[i]["retweeted_status"]["quoted_status"]['extended_tweet']['full_text']
						duplicate_text_remover.add(tweet_3)
						counter[i]=1
						count+=1

		if'extended_tweet' in Tweet_List[i].keys():
			if 'full_text' in Tweet_List[i]['extended_tweet'].keys():
				tweet_4=Tweet_List[i]['extended_tweet']['full_text']
				duplicate_text_remover.add(tweet_4)
				counter[i]=1
				count+=1
		for j in duplicate_text_remover:
			concat_tweet=concat_tweet+j+" "
		final_tweet_texts[i]=concat_tweet
		final_tweet_timestamps[i]=str(Tweet_List[i]['timestamp_ms'])
		final_tweet_ids[i]=str(Tweet_List[i]['id'])

	text_list=[]

	for i in range(len(Tweet_List)):
		if counter[i]!=1:
			text_list.append(i)

	for i in text_list:
		final_tweet_texts[i]=Tweet_List[i]['text']
		final_tweet_timestamps[i]=str(Tweet_List[i]['timestamp_ms'])
		final_tweet_ids[i]=str(Tweet_List[i]['id'])
		# print(Tweet_List[i]['text'],i)
	print(len(final_tweet_texts))
	print(len(final_tweet_timestamps))
	print(len(final_tweet_ids))
	return final_tweet_texts,final_tweet_timestamps, final_tweet_ids

############ testing 

# month="04"
# year="2020"
# day="28"
# serial="001"


# myfile="../Data/"+"covid-cardio-tweets-"+year+"-"+month+"-"+day+"-"+serial+".json"
# Tweets=get_tweets(myfile)
# print(Tweets)
