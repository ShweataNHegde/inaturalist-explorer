import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_json(json_file):
    with open(json_file, encoding='utf-8') as f:
        metadata_in_json = json.load(f)
        list_of_keyword_list = (metadata_in_json['keywords'])
    return list_of_keyword_list

def remove_empty_list(list_of_keyword_list):
    clean_list  = [x for x in list_of_keyword_list if x]
    return clean_list

def flatten_list(list_of_keyword_list):
    flat_list = []
    for sublist in list_of_keyword_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def remove_not_strings(flat_list):
    b = [item for item in flat_list if type(item) is str]
    return b


def make_histogram(label_count_dict):
     plt.figure()
     df = pd.DataFrame.from_dict(label_count_dict, orient='index')
     df.plot(kind='bar')
     plt.savefig('test_2.png')


def make_count_table(keywords_list, path = 'counts.csv'):
    labels, counts = np.unique(keywords_list,return_counts=True)
    label_count_dict = {}
    label_count_dict['labels'] = labels
    label_count_dict['counts'] = counts
    df = pd.DataFrame(label_count_dict).sort_values(by='counts', ascending=False)
    df.to_csv(path, encoding='utf-8', line_terminator='\r\n')
    return label_count_dict
   
 
def main():
    keywords_list = read_json('results/i_naturalist_results_json_file_test_nan.json')
    clean_list_with_no_nan = remove_empty_list(keywords_list)
    flattened_keyword_list = flatten_list(clean_list_with_no_nan)
    clean_only_strings_list = remove_not_strings(flattened_keyword_list)
    #print(clean_only_strings_list)
    label_count_dict = make_count_table(clean_only_strings_list)
    make_histogram(label_count_dict)

main()
    
