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
import trapdoor_manager
import encryption_manager
import pickle
import json
import pprint
import time

def create_index(filelist):
    create_dictionary(filelist)



def create_dictionary(filelist):
    inverted_index = {}

    # loop files in the directory
    os.chdir('../testdocuments')
    fileList = os.listdir(os.getcwd())
    appearances_dict = dict()
    documentlist = []  # document list for tfidf
    try:
        print(f"---Data prep-process started---")
        start_time_prep_process = time.time()
        for file in fileList:
            print(file)
            sentence = ""
            # read data from CSV
            if file.endswith('.csv'):
                with open(file, 'r', encoding='utf-8') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader, None)  # skip the headers

                    #non_empty_rows = sum(1 for row in csv_file if row.strip())

                    for row in csv_reader:
                        # If non-empty, but incomplete lines should be ignored:
                        if len(row) < 3:
                            continue

                        all_lowercase = all_lower(row)
                        filtered_words = remove_stop_words(all_lowercase)
                        stemmed_words = stem_word_list(filtered_words)
                        pre_precessed = remove_special_characters(stemmed_words)

                        # create document list for tfidf
                        sentence = sentence+" ".join(pre_precessed)+" "

                        word_frequency = {}
                        for word in pre_precessed:

                            term_frequency = appearances_dict[word].frequency if word in appearances_dict else 0
                            temp_file = appearances_dict[word].docName if word in appearances_dict else ''

                            if file in temp_file:
                                None
                            else:
                                temp_file = (temp_file + " " + file)
                            appearances_dict[word] = utils.appearance.Appearance(temp_file, term_frequency + 1, '')

                            if word not in word_frequency:
                                word_frequency[word] = 1
                            else:
                                word_frequency[word] += 1

                        for word, frequency in word_frequency.items():
                            if word not in inverted_index:
                                inverted_index[word] = []
                            inverted_index[word].append((file, frequency))

                    end_time_prep_process = time.time()
                    elapsed_time_prep_process = end_time_prep_process - start_time_prep_process
                    print(f"-------Data prep-process ended with {elapsed_time_prep_process} seconds-----------")
                documentlist.append(sentence)  # add content to tfidf document list
    except Exception:
        print("########################### Exception occured -------------- ")

    # print("end")
    # generate tfidf
    print("--- Generate tfidf vectorizer started ---")
    start_time_tfidf = time.time()
    sorted_word_tfidf = utils.tf_idf_words.generate_tfidf_vectorizer(documentlist)
    end_time_tfidf = time.time()
    elapsed_time_tfidf = end_time_tfidf - start_time_tfidf
    print(f"--- Generate tfidf vectorizer ended with {elapsed_time_tfidf} seconds ---")

    # create bloom filter
    print("--- Generate bloom filter started ---")
    start_time_boolf = time.time()
    keys_list = list(sorted_word_tfidf.keys())
    utils.bloom_test.addItemsToFilter(keys_list)
    end_time_boolf = time.time()
    elapsed_time_boolf = end_time_boolf - start_time_boolf
    print(f"--- Generate bloom filter ended with {elapsed_time_boolf} seconds ---")

    # create inverted index
    print("--- Create inverted index started ---")
    start_time_invindx = time.time()
    create_inverted_index(appearances_dict, keys_list)
    end_time_invindx = time.time()
    elapsed_time_invindx = end_time_invindx - start_time_invindx
    #print(*sorted_word_tfidf, sep=' >> \n')
    print(f"--- Create inverted index ended with {elapsed_time_invindx} seconds---")

    return appearances_dict


def create_inverted_index(appearances_dict, keys_list):

    sorted_data = {key: appearances_dict[key] for key in keys_list if key in appearances_dict}

    for key, value in sorted_data.items():
        value.tag = trapdoor_manager.create_tag(key)


    # Convert JSON string to bytes
    # dict_str = json.dumps(sorted_data)
    # bytes_data = dict_str.encode('utf-8')
    # data = bytes_data

    # json_string = json.dumps(sorted_data)
    # bytes_string = json_string.encode()

    dictionary_string = pprint.pformat(sorted_data)

    #encrypt index and save file
    print("--- encrypt file content started ---")
    start_time_encrypt = time.time()
    encryption_manager.encrypt_file_content(dictionary_string, "index")
    end_time_encrypt = time.time()
    elapsed_time_encrypt = end_time_encrypt - start_time_encrypt
    print(f"--- encrypt file content ended with {elapsed_time_encrypt} seconds---")

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
