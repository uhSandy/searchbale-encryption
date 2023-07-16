import Manager.trapdoor_manager
import bloom_test
import Manager.encryption_manager
import json
import ast
import time

def searchKeys(secretkey, searchKeys):
    print("------------------Search started")
    start_time_search = time.time()
    #get trapdoor values
    print("------------------Getting trap door values")
    trapdoorkeys = calltrapdoor(searchKeys)

    #find files for keywords from inverted index
    getdatafiles(trapdoorkeys, secretkey)
    end_time_search = time.time()
    elapsed_time_search = end_time_search - start_time_search
    print(f"-------Data search ended with {elapsed_time_search} seconds-----------")

def calltrapdoor(searchKeys):
    keywordtags = []
    for searchkey in searchKeys:
        tag = Manager.trapdoor_manager.create_tag(searchkey)
        keywordtags.append(tag)

    #print(keywordtags)
    #call bllom filter
    print("------------------Check search key values exists using bloom filter")
    exisistingwords = bloom_test.searchWords(keywordtags)
    #print(exisistingwords)
    return exisistingwords


def getdatafiles(trapdoorkeys, secretkey):

    #decrypt index file
    print("------------------Decrypt index")
    decrypteddata = Manager.encryption_manager.decryptFile("../data/index_encrypted.bin", secretkey)

    dictionary_data = json.loads(decrypteddata)

    getfilesincluding(trapdoorkeys, dictionary_data)


def getfilesincluding(trapdoorkeys, dictionary_data):
    #print("=======#######====================================================")
    #print(dictionary_data)
    #print(trapdoorkeys)
    print("------------------Get match files data")
    matchfiles = search_value(dictionary_data, "tag", trapdoorkeys)

    print(matchfiles)
    # if search_value(dictionary_data, "tag", trapdoorkeys):
    #     print("At least one of the search values exists for the given key in the dictionary.")
    # else:
    #     print("None of the search values exist for the given key in the dictionary.")


def search_value(dictionary, searchkey, values):
    matches = {}

    dictionaryd = ast.literal_eval(dictionary)
    if isinstance(dictionaryd, dict):
        for key, sub_dict in dictionaryd.items():
            #print(sub_dict[searchkey])
            #print(sub_dict[searchkey] in values)
            if searchkey in sub_dict and sub_dict[searchkey] in values:
                matches[key] = sub_dict['docName']

    return matches


searchKeys('', ['doppler', 'intermittent', 'cool', 'bed', 'ashen', 'doppler', 'wiggle', 'cool', 'bed', 'ashen',
                'resistance', 'intermittent', 'incisional', 'hazard', 'ashen', 'resistance', 'intermittent', 'incisional', 'hazard', 'ashen',
'doppler', 'wiggle', 'cool', 'bed', 'ashen', 'resistance', 'intermittent', 'incisional', 'hazard','ashen',
'chloride', 'tartrate', 'metoprolol', 'replacement', 'chloride', 'resistance', 'intermittent', 'incisional', 'hazard', 'ashen',
                'chloride', 'tartrate', 'metoprolol', 'replacement', 'chloride', 'resistance', 'negative', 'xxx', 'trachomatis', 'assay',
'chloride', 'tartrate', 'metoprolol', 'replacement', 'chloride', 'resistance', 'negative', 'xxx', 'trachomatis', 'assay',
                'chloride', 'negative', 'eia', 'replacement', 'chloride', 'amplification', 'negative', 'xxx', 'range', 'negative',
 'chloride', 'nucleic', 'eia', 'reference', 'interpretation', 'amplification', 'indicative', 'xxx', 'range', 'negative',
'chloride', 'right', 'eia', 'reference', 'magnesium', 'amplification', 'infection', 'xxx', 'range', 'negative',
                'chloride', 'gram', 'eia', 'reference', 'negative', 'amplification', 'infection', 'budding', 'isolated', 'mrsa',
                ])
