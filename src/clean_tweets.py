import json
from tqdm import tqdm
from remove_names import remove_names
from utils import get_start_indices, divide_in_chunks, remove_garbage


def split_by_start_ind(raw_words_list, start_index):
    clean_split_list = []
    joint = "".join(raw_words_list)
    for i in range(len(start_index) - 1):
        clean_split_list.append(joint[start_index[i]: start_index[i + 1] - 1])
    clean_split_list.append(joint[start_index[-1]:-1])
    return clean_split_list


with open("../Tweets/Extracted.txt", 'r') as f:
    tweets = json.load(f)
# tweets = tweets[0:300]
print("No. of tweets: ", len(tweets))
text_list = [tweet['text'] for tweet in tweets]

text_list = list(map(remove_garbage, text_list))
CHUNK_SIZE = 110
start_index = get_start_indices(text_list)
raw_words_list = divide_in_chunks(text_list, CHUNK_SIZE)

lens = [len(data.split()) for data in raw_words_list]
max_ind = lens.index(max(lens))
print("Maximum length of a chunk:", max(lens), "at index: ", max_ind)

for i in tqdm(range(len(raw_words_list))):
    # if i != max_ind:  # For tuning chunk size
    #     continue

    replaced_text = remove_names(raw_words_list[i])
    with open("../Bio_Yodie/Replaced_text/replaced-text_" + str(i), "w") as f:
        f.write(replaced_text)

    assert len(raw_words_list[i]) == len(replaced_text)
    raw_words_list[i] = replaced_text

clean_split_list = split_by_start_ind(raw_words_list, start_index)
clean_split_list = list(map(remove_garbage, clean_split_list))
for i in range(len(tweets)):
    tweets[i]['text'] = clean_split_list[i]

with open("../Tweets/clean_tweets_final.json", 'w') as f:
    json.dump(tweets, f)

print("done")
