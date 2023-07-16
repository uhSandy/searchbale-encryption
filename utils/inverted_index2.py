import os
import csv
import read_csv

def createDictionary():
    wordsAdded = {}
    cwd = os.getcwd()
    os.chdir('../documents')
    fileList = os.listdir(os.getcwd())

    for file in fileList:
        #read data from CSV
        with open(file, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)  # skip the headers

            for row in csv_reader:
                # If non-empty, but incomplete lines should be ignored:
                if len(row) < 3:
                    continue

                all_lowercase = read_csv.all_lower(row)
                filtered_words = read_csv.remove_stop_words(all_lowercase)
                stemmed_words = read_csv.stem_word_list(filtered_words)
                pre_precessed = read_csv.remove_special_characters(stemmed_words)

                for word in pre_precessed:
                    print(">>>>>>>>> "+word)
                    #processed_word = read_csv.stem_further(word)
                    #print("------------ "+test)
                    if word not in wordsAdded.keys():
                        wordsAdded[word] = [csv_file.name]

                    else:
                        if file not in wordsAdded[word]:
                            wordsAdded[word] += [csv_file.name]

    return wordsAdded, cwd


def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('../documents/index-file.txt', 'w') as indexFile:

        for word, files in words.items():
            indexFile.write(word + " ")
            for file in files:
                indexFile.write(file[:file.find(".txt")] + " ")

            indexFile.write(f'{len(files)}\n')


writeToFile(*createDictionary())