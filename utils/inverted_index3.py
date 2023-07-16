import os
import csv
import read_csv
import utils.appearance

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
                    #print(">>>>>>>>> "+word)
                    #processed_word = read_csv.stem_further(word)
                    #print("------------ "+test)
                    if word not in wordsAdded.keys():
                        wordsAdded[word] = [csv_file.name]

                    else:
                        if file not in wordsAdded[word]:
                            wordsAdded[word] += [csv_file.name]

    return wordsAdded, cwd


def writeToFile(words, cwd):
    print(">>>>>>>>> " + cwd)
    os.chdir(cwd)
    appearances_dict = dict()
    fileNames = ''
    with open('../documents/index-file.txt', 'w') as indexFile:

        for word, files in words.items():
            indexFile.write(word + " ")
            fileNames = ''
            for file in files:
                #print(file[:file.find(".txt")] + " ")
                fileNames = fileNames + " " + file[:file.find(".txt")]
                indexFile.write(file[:file.find(".txt")] + " ")

            #print(fileNames)
            indexFile.write(f'{len(files)}\n')


            term_frequency = appearances_dict[word].frequency if word in appearances_dict else 0
            appearances_dict[word] = utils.appearance.Appearance(word, fileNames, (term_frequency + 1), len(files))
            #word, doc_name, frequency, document_count
            print(word, fileNames, (term_frequency + 1), len(files))


        print(appearances_dict)


writeToFile(*createDictionary())