import os
import csv
import read_csv
import utils.appearance
import utils.bloom_test

def create_inverted_index():
    inverted_index = {}
    #loop files in the directory
    os.chdir('../helper')
    fileList = os.listdir(os.getcwd())
    appearances_dict = dict()

    for file in fileList:

        # read data from CSV
        if file.endswith('.csv'):
            with open(file, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader, None)  # skip the headers

                for row in csv_reader:
                    print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
                    # If non-empty, but incomplete lines should be ignored:
                    if len(row) < 3:
                        continue

                    all_lowercase = read_csv.all_lower(row)
                    filtered_words = read_csv.remove_stop_words(all_lowercase)
                    stemmed_words = read_csv.stem_word_list(filtered_words)
                    pre_precessed = read_csv.remove_special_characters(stemmed_words)

                    utils.bloom_test.addItemsToFilter(pre_precessed)

                    word_frequency = {}
                    for word in pre_precessed:

                        term_frequency = appearances_dict[word].frequency if word in appearances_dict else 0
                        temp_file = appearances_dict[word].docName if word in appearances_dict else ''

                        if file in temp_file: None
                        else: temp_file = (temp_file+ " " + file)
                        appearances_dict[word] = utils.appearance.Appearance(temp_file, term_frequency + 1)

                        if word not in word_frequency:
                            word_frequency[word] = 1
                        else:
                            word_frequency[word] += 1

                    for word, frequency in word_frequency.items():
                            if word not in inverted_index:
                                inverted_index[word] = []
                            inverted_index[word].append((file, frequency))

    print("++++++++++++++++++++++++++++++++")
    print(appearances_dict)
    return appearances_dict



# Example documents
documents = {
    "document1.txt": "This is the first document.",
    "document2.txt": "This second document is the second document.",
    "document3.txt": "And this is the second third one .",
}

# Create the inverted index
index = create_inverted_index()

# Print the inverted index
# for word, entries in index.items():
#     print("Word:", word)
#     for filename, frequency in entries:
#         print("  Filename:", filename)
#         print("  Frequency:", frequency)
#     print()