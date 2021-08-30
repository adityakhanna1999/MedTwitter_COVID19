from requests.auth import HTTPBasicAuth
import requests


def remove_names(data):
    url = "https://cloud-api.gate.ac.uk/process-document/twitie-named-entity-recognizer-for-tweets"
    user = 'gcehixrnvnia'
    password = 'j8hbkb7jfl1s8jpvvezc'
    headers = {'Content-type': 'text/plain'}
    annotations = [":Person", ":Organization", ":Address"]

    url = url + "?"
    for i in annotations:
        url = url + "annotations=" + i + "&"
    url = url[:-1]

    response = requests.post(url,
                             auth=HTTPBasicAuth(user, password),
                             headers=headers,
                             data=data)
    response = response.json()
    initial_length = len(data)
    # data = bytearray(data, 'UTF-8')
    data_list = list(data)
    # print("Length is: ", initial_length)
    try:
        entities = response['entities']
        for entity in entities:
            keywords = entities[entity]
            for keyword in keywords:
                start_index = keyword['indices'][0]
                # print(start_index)
                # data[start_index:start_index + 1] = bytearray('@', 'UTF-8')
                data_list[start_index] = '@'
                # print()

        # data = data.decode('UTF-8')
        data = "".join(data_list)
        final_length = len(data)
        assert initial_length == final_length
        return data
    except KeyError as e:
        print("Failed", response, e)
        exit(0)


if __name__ == "__main__":
    data = "Hi I am ?"
    print(remove_names(data))



