import csv
import re


def load_csv(csv_file_path):
    l = {}
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            l[row[0]] = {
                'broader': row[1],
                'prefLabel': row[2]
            }

    return l


def matcher(dict1, dict2):
    for k1, v1 in dict1.items():
        words_1 = v1['prefLabel'].split(' ')
        for k2, v2 in dict2.items():
            words_2 = v2['prefLabel'].split(' ')

            for w in words_1:
                if w in words_2:
                    print(k1 + ', ' + k2)


agift_concepts = load_csv('agift-concepts.csv')
crs_concepts = load_csv('crs-th-concepts.csv')

matcher(agift_concepts, crs_concepts)
#
# import pprint
# pprint.pprint(agift_concepts)

#print(agift_concepts['https://data.naa.gov.au/def/agift/Workplace-training']['prefLabel'])
