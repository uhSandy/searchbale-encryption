import Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
import json

import json

# Convert dictionary to JSON string
# data = {'key1': 'value1', 'key2': 'value2'}
# json_string = json.dumps(data)
#
# # Convert JSON string to bytes
# bytes_string = json_string.encode()
#
# # Print the bytes string
# print("............................................................")
# print(bytes_string)
# print("-----------------------------------------------------------")
# Generate or load RSA key pair
# key = RSA.generate(2048)
# private_key = key.export_key()
# public_key = key.publickey().export_key()
#
# # Encrypt a dictionary
# data = {'test': {'docName': ' Book1.csv', 'frequency': 1}, 'test2': {'docName': ' Book1.csv', 'frequency': 1}, 'test3': {'docName': ' Book1.csv', 'frequency': 1}, 'cefepim': {'docName': ' Book1.csv emartemp.csv', 'frequency': 3}, 'b': {'docName': ' Book1.csv', 'frequency': 1}, 'c': {'docName': ' Book1.csv', 'frequency': 1}, 'e': {'docName': ' Book1.csv', 'frequency': 1}, 'f': {'docName': ' Book1.csv', 'frequency': 1}, 'magnesium': {'docName': ' emartemp.csv', 'frequency': 12}, 'sulf': {'docName': ' emartemp.csv', 'frequency': 12}, 'p26pkf': {'docName': ' emartemp.csv', 'frequency': 1}, 'potassium': {'docName': ' emartemp.csv', 'frequency': 9}, 'chloride': {'docName': ' emartemp.csv', 'frequency': 5}, 'replacement': {'docName': ' emartemp.csv', 'frequency': 7}, 'critical': {'docName': ' emartemp.csv', 'frequency': 18}, 'care': {'docName': ' emartemp.csv', 'frequency': 18}, 'oncolog': {'docName': ' emartemp.csv', 'frequency': 7}, 'metoprolol': {'docName': ' emartemp.csv', 'frequency': 4}, 'tartr': {'docName': ' emartemp.csv', 'frequency': 4}, 'morphine': {'docName': ' emartemp.csv', 'frequency': 2}, 'p33k2x': {'docName': ' emartemp.csv', 'frequency': 1}, 'lidocaine': {'docName': ' emartemp.csv', 'frequency': 2}, '1': {'docName': ' emartemp.csv', 'frequency': 2}, 'sulfate': {'docName': ' emartemp.csv', 'frequency': 2}, 'fentanyl': {'docName': ' emartemp.csv', 'frequency': 3}, 'citr': {'docName': ' emartemp.csv', 'frequency': 3}, 'chlorid': {'docName': ' emartemp.csv', 'frequency': 4}, 'quetiapine': {'docName': ' emartemp.csv', 'frequency': 2}, 'fumar': {'docName': ' emartemp.csv', 'frequency': 2}, 'p54tss': {'docName': ' emartemp.csv', 'frequency': 2}, 'p851dg': {'docName': ' emartemp.csv', 'frequency': 1}, 'p14csq': {'docName': ' emartemp.csv', 'frequency': 1}, 'insulin': {'docName': ' emartemp.csv', 'frequency': 1}, 'p28ev2': {'docName': ' emartemp.csv', 'frequency': 1}, 'picc': {'docName': ' emartemp.csv', 'frequency': 1}, 'midline': {'docName': ' emartemp.csv', 'frequency': 1}, 'insert': {'docName': ' emartemp.csv', 'frequency': 1}, 'heparin': {'docName': ' emartemp.csv', 'frequency': 1}, 'calcium': {'docName': ' emartemp.csv', 'frequency': 22}, 'gluconate': {'docName': ' emartemp.csv', 'frequency': 11}, 'sliding': {'docName': ' emartemp.csv', 'frequency': 11}, 'scale': {'docName': ' emartemp.csv', 'frequency': 11}, 'ionized': {'docName': ' emartemp.csv', 'frequency': 11}}
# json_data = json.dumps(data).encode()
#
# cipher = PKCS1_v1_5.new(RSA.import_key(public_key))
# encrypted_data = cipher.encrypt(json_data)
# print(encrypted_data)
#
# # Save encrypted data to a file
# with open('encrypted_data.txt', 'wb') as file:
#     file.write(encrypted_data)

# Write two bytes data to a text file
# byte_data = b'4}\x07JS\x8f\n\xaf\x83lE\xef|{\x804\xc5\x07\xc9\x8d\x12\xcf\xf5`J0\xdfd\x12\xd3M\x8a\xe2\xa8\xdb\xaau\x9e3uV\xe1\xf0\xf9\xf9\x0f\x82;\x80\xc4\xf4R\x9d\xcbj\x87\xc9\x00\x02\xd1E\x8c\xef\xa9+TH\x14\x03\xbb\xa6\xae\x1bvX\xfe,i\xb8~\xbe\x86\x86\xd9\xe75\xfb\xb6\xf6}b\xb3\x98\x10\xb1\x97\x10\x94\x13\xdb\xef\xa1\xa3HR \xbd\x00\xce\xeb\x8c\xa8\x13\xd9`\x97A\xa7\t\xd6\x85\x08\x07]\x190\x18\x83\xcfvJe\xa8$\x81\x14\x1a\x0b\xe3\x99N\xb4\xa8p1\xd4TXH\xe9\x05\xe5{\xfe\xc7\x95N\n\xfcA\xeb\x11\xd1e%L\xa5\xf8`\xc9\xa4\xc3ka\xa6\x9b!4{\x05]\xa6%\xb5x\xa7\x91\x11\xb8\xbd\xee+\xbeR\x1f\x07\x8d\xe5*O\xd5u!\xf8U\x1bq\xb6,\x91\xa2h\xdd0\x1eH\xe8\xb3iw\x7f||\xb1\x8e\x08\x95\x18\x89\xea\x8ff\x99\x9b\x12\x9c\xc0P.\xf40\xe4\xcb\xb2\x9d\xb2.`H\x93\xae>\x9c\x9c\xf4c'
# with open('data.bin', 'wb') as file:
#     file.write(byte_data)
#
# with open('data.bin', 'rb') as file:
#     byte_data = file.read()
#
#
#
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(byte_data)

# keywordtags = []
# tag = 12779158712373313182466584282706366992391653073770612241046994659128135082755968519749908812492964360311061571327401026405866873731053887217531528253723542
# keywordtags.append(tag)
#
# tag = 134
# keywordtags.append(tag)
# print(keywordtags)

# def search_value(dictionary, key, values):
#     matches = []
#     if isinstance(dictionary, dict):
#         if key in dictionary and dictionary[key] in values:
#             matches.append(dictionary[key])
#         for sub_dict in dictionary.values():
#             if isinstance(sub_dict, dict):
#                 matches.extend(search_value(sub_dict, key, values))
#     return matches
#
# # Example dictionary
# my_dict = {
#     'key1': {
#         'subkey1': 'value1',
#         'subkey2': 'value2',
#     },
#     'key2': {
#         'subkey3': 'value1',
#         'subkey4': 'value4',
#     },
#     'key3': {
#         'subkey5': 'value2',
#         'subkey6': 'value2',
#     }
# }
# print(type(my_dict))
# search_key = 'subkey2'
# search_values = ['value1', 'value2']
#
# # Find the specific values from the sub-dictionaries that match any of the search values for the given key
# matches = search_value(my_dict, search_key, search_values)
#
# # Print the matching values
# for match in matches:
#     print(match)


import os
import csv
import utils.appearance
import utils.bloom_test
import utils.tf_idf_words
import nltk
import re
from nltk.corpus import stopwords
nltk.data.path.append('../helper')
nltk.download('stopwords')
from nltk.stem import PorterStemmer


folder_path = '../testdocuments'  # Replace with the path to your folder

count = 0
# Loop through files in the folder
# loop files in the directory
os.chdir('../testdocuments')
fileList = os.listdir(os.getcwd())
appearances_dict = dict()
documentlist = []  # document list for tfidf

def all_lower(my_list):
    return [x.lower() for x in my_list]

def remove_stop_words(word_list):
    # Download the stopwords if not already downloaded
    nltk.download('stopwords')

    # Get the English stop words
    stop_words = set(stopwords.words('english'))

    # Remove stop words from the word list
    filtered_words = []
    for sentence in word_list:
        words = re.findall(r'\w+', sentence)  # Extract individual words from the sentence using regular expression
        filtered_words.append(' '.join([word for word in words if word.lower() not in stop_words]))

    return filtered_words

def stem_word_list(word_list):
    stemmer = PorterStemmer()
    stemmed_list = [stemmer.stem(word) for word in word_list]

    return stemmed_list

def remove_special_characters(words):
    special_char = '{}()[]'  # '{}()[].,:;+-*/&|<>=~$1234567890'
    s = [''.join(x for x in string if not x in special_char) for string in words]
    stemmed = stem_further(s)
    return stemmed

def stem_further(word_list):
    return_list = []
    for word in word_list:

        letters = re.findall('[a-zA-Z]', word)
        numbers = re.findall('[0-9]', word)
        stem_further = True

        if len(numbers) > len(letters):
            # print("The sentence contains more numbers than letters.")
            stem_further = False

        # print(stem_further)
        # print("=========== "+word)
        if (stem_further):
            return_list.extend(split_value_into_words(word))
        # else:
        #     return_list.append(word)

    # print(*return_list, sep=' >> \n')
    return return_list

def split_value_into_words(sentence):
    words = sentence.split()
    return words

    # create bloomfilter
    #utils.bloom_test.addItemsToFilter(preprocessed_content)

    # create index dictionary


    #generate tfidf for terms
    #generate_tfidf_vectorizer()
    remove_stop_words(['10008287', '22168393', '10008287-32', '32', '10008287-58', '', 'p26pkf', '9/28/2145 20:15', 'potassium chloride replacement (critical care and oncology)', '', '9/28/2145 20:15', '9/28/2145 20:38'])

def tst():
    # try:
        print(f"---Data prep-process started---")
        #######
        os.chdir('../testdocuments')
        fileList = os.listdir(os.getcwd())
        for file in fileList:
            #print("Startttttt+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # file = "../helper/emartemp.csv"
            #print(file)
            sentence = ""
            # read data from CSV
            testtemp1 = []
            testtemp2 = []
            testtemp1sen = ""
            testtemp2sen = ""
            if file.endswith('.csv'):
                with open(file, 'r', encoding='utf-8') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader, None)  # skip the headers

                    # non_empty_rows = sum(1 for row in csv_file if row.strip())

                    for row in csv_reader:
                        # If non-empty, but incomplete lines should be ignored:
                        if len(row) < 3:
                            continue

                        all_lowercase = all_lower(row)
                        filtered_words = remove_stop_words(all_lowercase)
                        stemmed_words = stem_word_list(filtered_words)
                        pre_precessed = remove_special_characters(stemmed_words)

                        # testtemp1.extend(all_lowercase)
                        # testtemp2.extend(pre_precessed)
                        testtemp1sen = testtemp1sen + " ".join(all_lowercase) + " "
                        testtemp2sen = testtemp2sen + " ".join(pre_precessed) + " "

                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                testtemp1 = testtemp1sen.split()
                print("@@@@@@@@@@@@@@@@@@@@@@@@")
                testtemp2 = testtemp2sen.split()
                truepositive = 0
                truenegative = 0
                falsepositive = 0
                falsenegative = 0
                for sec in testtemp2:
                    if sec in testtemp1:
                        #print(f"{sec} is present in the list.")
                        # truepositive
                        truepositive = truepositive + 1
                    else:
                        # print(f"{sec} is not present in the list.")
                        # truenegative
                        truenegative = truenegative + 1

                for sec1 in testtemp1:
                    letters = re.findall('[a-zA-Z]', sec1)
                    numbers = re.findall('[0-9]', sec1)
                    hasmorestring = True

                    if len(numbers) > len(letters):
                        # print("The sentence contains more numbers than letters.")
                        hasmorestring = False

                    if (hasmorestring):
                        if sec1 in testtemp2:
                            # valid and valid
                            truepositive = truepositive + 1
                        else:
                            # vaild but not there = FalseNegative
                            falsenegative = falsenegative + 1
                    else:
                        # have more numbers
                        if sec1 in testtemp2:
                            # false positive
                            falsepositive = falsepositive + 1

                print("1111111 truepositive")
                print(truepositive)
                print("22222222 truenegative")
                print(truenegative)
                print("3333333 falsepositive")
                print(falsepositive)
                print("4444444 falsenegative")
                print(falsenegative)
    # except Exception:
    #     print("########################### Exception occured -------------- ")

tst()