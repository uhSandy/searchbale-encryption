import re
import os
import csv
import utils.read_csv
import utils.appearance
import utils.in_memoryDb
import utils.inverted_index


class InvertedIndex4:
    """
    Inverted Index class.
    """

    def __init__(self, db):
        self.index = dict()
        self.db = db

    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index)


    def createDictionary(self):
        wordsAdded = {}
        cwd = os.getcwd()
        os.chdir('../documents')
        fileList = os.listdir(os.getcwd())

        for file in fileList:
            # read data from CSV
            with open(file, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader, None)  # skip the headers

                for row in csv_reader:
                    # If non-empty, but incomplete lines should be ignored:
                    if len(row) < 3:
                        continue

                    all_lowercase = utils.read_csv.all_lower(row)
                    filtered_words = utils.read_csv.remove_stop_words(all_lowercase)
                    stemmed_words = utils.read_csv.stem_word_list(filtered_words)
                    pre_precessed = utils.read_csv.remove_special_characters(stemmed_words)

                    for word in pre_precessed:
                        #print(">>>>>>>>> " + word)
                        # processed_word = read_csv.stem_further(word)
                        # print("------------ "+test)
                        if word not in wordsAdded.keys():
                            wordsAdded[word] = [csv_file.name]

                        else:
                            if file not in wordsAdded[word]:
                                wordsAdded[word] += [csv_file.name]

        return wordsAdded, cwd

    def writeToFile(self, words, cwd):
        os.chdir(cwd)
        appearances_dict = dict()
        fileNames = ''
        with open('../documents/index-file.txt', 'w') as indexFile:

            for word, files in words.items():
                indexFile.write(word + " ")
                fileNames = ''
                for file in files:
                    # print(file[:file.find(".txt")] + " ")
                    fileNames = fileNames + " " + file[:file.find(".txt")]
                    indexFile.write(file[:file.find(".txt")] + " ")

                # print(fileNames)
                indexFile.write(f'{len(files)}\n')

                term_frequency = appearances_dict[word].frequency if word in appearances_dict else 0
                appearances_dict[word] = utils.appearance.Appearance(word, fileNames, (term_frequency + 1), len(files))
                # word, doc_name, frequency, document_count
                print(word, fileNames, (term_frequency + 1), len(files))

                # Update the inverted index
                update_dict = {key: [appearance]
                if key not in self.index
                else self.index[key] + [appearance]
                               for (key, appearance) in appearances_dict.items()}
                self.index.update(update_dict)

                print(">>>>>> " + str(self.index))
                # Add the document into the database
                #self.db.add(document)

            print(appearances_dict)



    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """
        #doc_path = './documents'

        # Remove punctuation from the text.
        clean_text = re.sub(r'[^\w\s]', '', document['text'])
        terms = clean_text.split(' ')
        appearances_dict = dict()
        # Dictionary with each term and the frequency it appears in the text.
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = utils.appearance.Appearance(document['id'], term_frequency + 1)

        # Update the inverted index
        update_dict = {key: [appearance]
        if key not in self.index
        else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items()}
        self.index.update(update_dict)

        print(">>>>>> "+ str(self.index))
        # Add the document into the database
        self.db.add(document)
        return document

    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances.
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        return {term: self.index[term] for term in query.split(' ') if term in self.index}

    #writeToFile(*createDictionary())
    utils.in_memoryDb = utils.in_memoryDb.InMemoryDb()

