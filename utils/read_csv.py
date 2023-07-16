import csv
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def all_lower(my_list):
    return [x.lower() for x in my_list]


def remove_stop_words(word_list):
    # Download the stopwords if not already downloaded
    nltk.download('stopwords')

    # Get the English stop words
    stop_words = set(stopwords.words('english'))

    # Remove stop words from the word list
    filtered_list = [word for word in word_list if word.lower() not in stop_words]

    return filtered_list


def stem_word_list(word_list):
    stemmer = PorterStemmer()
    stemmed_list = [stemmer.stem(word) for word in word_list]
    return stemmed_list

def remove_special_characters(words):
    special_char = '{}()[]'#'{}()[].,:;+-*/&|<>=~$1234567890'
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
            #print("The sentence contains more numbers than letters.")
            stem_further = False

        #print(stem_further)
        #print("=========== "+word)
        if(stem_further):
            return_list.extend(split_value_into_words(word))
        else:
            return_list.append(word)

    #print(*return_list, sep=' >> \n')
    return return_list


def split_value_into_words(sentence):
    words = sentence.split()
    return words


def read_csv_file(file_path):
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)#skip the headers
        for row in csv_reader:
            print(row)
            # all_lowercase = all_lower(row)
            # filtered_words = remove_stop_words(all_lowercase)
            # stemmed_words = stem_word_list(filtered_words)
            # pre_preocessed = remove_special_characters(stemmed_words)

            #print(pre_preocessed)
            #return all_lowercase

# Provide the path to your CSV file
#csv_file_path = '../documents/emartemp.csv'

# Call the function to read and output the rows
#read_csv_file(csv_file_path)

