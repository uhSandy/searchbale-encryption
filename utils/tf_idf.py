import math

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

document1 = "Piford provide Hasa training to test working test test Professionals" #  "The beer drinking big sharks of Belgium drink beer."
document2 = "Piford  Hasa provide Hasa training to Hasa test students"  # "Belgium has great beer. They drink beer all the time."

response = tfidf.fit_transform([document1, document2])

print(len(tfidf.vocabulary_))
print(tfidf.vocabulary_)
print(response)
