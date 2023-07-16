import hashlib
from Crypto.PublicKey import RSA
import utils.tf_idf_words

# Function to generate SHA-256 hash of a keyword
def hash_keyword(keyword):
    hash_object = hashlib.sha256(keyword.encode())
    return int(hash_object.hexdigest(), 16)

# Function to create a tag for a keyword using a polynomial evaluation approach
# Define the polynomial coefficients
polynomial = [2, 3, 1]
def create_tag(keyword):
    hashed_keyword = hash_keyword(keyword)
    tag = 0
    #print(hashed_keyword)
    for i, coefficient in enumerate(polynomial):
        tag += coefficient * (hashed_keyword ** i)
        #print("coefficient %s " % coefficient)
        #print("tag %s " % tag)
    return tag

# Function to perform a search using the trapdoor and polynomial evaluation
def perform_search(trapdoor, inverted_index):
    matching_keywords = []
    for keyword, tag in inverted_index.items():
        if tag == trapdoor:
            matching_keywords.append(keyword)
    return matching_keywords

# Example usage

#print(create_tag("care"))

# Create an inverted index with keyword-tag pairs
# inverted_index = {
#     'apple': create_tag('apple', polynomial),
#     'banana': create_tag('banana', polynomial),
#     'orange': create_tag('orange', polynomial)
# }
#
# # Generate a trapdoor for the search query (e.g., 'apple')
# trapdoor = create_tag('apple', polynomial)
#
# # Perform the search using the trapdoor and polynomial evaluation
# matching_keywords = perform_search(trapdoor, inverted_index)
#
# print("Matching Keywords:")
# for keyword in matching_keywords:
#     print(keyword)

print(create_tag("test"))