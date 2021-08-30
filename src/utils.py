def flatten_json(y): 
    out = {} 
  
    def flatten(x, name =''): 
        # If the Nested key-value  
        # pair is of dict type 
        if type(x) is dict: 
            for a in x: 
                flatten(x[a], name + a + '&') 
        # If the Nested key-value 
        # pair is of list type 
        elif type(x) is list: 
            i = 0
            for a in x:                 
                flatten(a, name + str(i) + '&') 
                i += 1
        else: 
            out[name[:-1]] = x 
  
    flatten(y) 
    return out


def divide_in_chunks(list_1, chunk_size):
    extended = []
    temp = ""
    for i in range(len(list_1)):
        if i % chunk_size == 0 and i != 0:
            extended.append(temp)
            temp = ""
        temp += (list_1[i] + " ")
    extended.append(temp)
    return extended


def get_start_indices(p):
    count = 0
    start_index = []
    for i in range(len(p)):
        start_index.append(count)
        count += (len(p[i]) + 1)
    return start_index


def remove_garbage(input_string):
    input_string = input_string.encode('ascii', 'ignore').decode('ascii')
    words = input_string.split()
    output_list = [i for i in words if '@' not in i and '&' not in i and "https://" not in i]
    output = " ".join(output_list)
    return output
