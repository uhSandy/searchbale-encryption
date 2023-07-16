#from utils.bloom_filter import BloomFilter
from random import shuffle
from pybloom_live import BloomFilter
import pickle
import Manager.trapdoor_manager

n = 20  # no of items to add
p = 0.05  # false positive probability

# bloomf = BloomFilter(n, p)
# print("Size of bit array:{}".format(bloomf.size))
# print("False positive Probability:{}".format(bloomf.fp_prob))
# print("Number of hash functions:{}".format(bloomf.hash_count))

# words to be added
word_present = ['abound', 'abounds', 'abundance', 'abundant', 'accessible',
                'bloom', 'blossom', 'bolster', 'bonny', 'bonus', 'bonuses',
                'coherent', 'cohesive', 'colorful', 'comely', 'comfort',
                'gems', 'generosity', 'generous', 'generously', 'genial']

# word not added
# word_absent = ['bluff', 'cheater', 'hate', 'war', 'humanity',
#                'racism', 'hurt', 'nuke', 'gloomy', 'facebook',
#                'geeksforgeeks', 'twitter']

# Create and populate a Bloom filter
bloom_filter = BloomFilter(capacity=50000, error_rate=0.1)

filename = "../data/bloom_filter.bin"

def addItemsToFilter(wordslist):
    for item in wordslist:
        keywordtag = Manager.trapdoor_manager.create_tag(item)
        bloom_filter.add(keywordtag)

    # Save the Bloom filter to a file
    with open(filename, "wb") as file:
        pickle.dump(bloom_filter, file)

    print("added item to bloom filter")


def searchWords(searchwords):
    existingwords = []
    # Load the Bloom filter from the file
    with open(filename, "rb") as file:
        loaded_bloom_filter = pickle.load(file)

    for word in searchwords:
        #if bloomf.check(word):
        if word in loaded_bloom_filter:
            #print("'{}' is probably present!".format(word))
            existingwords.append(word)
        else:
            #print("'{}' is definitely not present!".format(word))
            status = "not present"

    return existingwords

###search with inverted index
    def search_document(self, document_id):
        if document_id in self.bloom_filter:
            return self.index.get(document_id)
        else:
            return None

# addItemsToFilter(['test', 'test2', 'test3', 'care', 'landon', 'cefepime', 'b', 'c'])
# searchWords(['test', 'care', 'landon'])
#shuffle(word_present)
#shuffle(word_absent)

# test_words = word_present[:10]
# shuffle(test_words)
# for word in test_words:
#     if bloomf.check(word):
#         print("'{}' is probably present!".format(word))
#     else:
#         print("'{}' is definitely not present!".format(word))