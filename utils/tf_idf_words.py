from sklearn.feature_extraction.text import TfidfVectorizer

def generate_tfidf_vectorizer(documents):
    # List of documents
    # documents = [
    #     "This is the first document.",
    #     "This document is the second document.",
    #     "And this is the third one.",
    #     "Is this the first document?",
    # ]
    #print(documents)

    # Create a TfidfVectorizer object
    tfidf_vectorizer = TfidfVectorizer()

    # Fit the vectorizer on the documents
    tfidf_vectorizer.fit(documents)

    # Get the list of words
    words = tfidf_vectorizer.get_feature_names_out()

    # Calculate the word frequencies across all documents
    word_frequencies = tfidf_vectorizer.transform(documents).toarray().sum(axis=0)

    # Calculate IDF for each word
    total_documents = len(documents)
    idf_values = [total_documents / (1 + freq) for freq in word_frequencies]

    # Calculate TF-IDF for each word
    tfidf_scores = tfidf_vectorizer.transform([" ".join(words)]).toarray()[0]

    # Create a dictionary to store word, IDF, and TF-IDF score pairs
    word_tfidf = {word: {"idf": idf, "tfidf": tfidf} for word, idf, tfidf in zip(words, idf_values, tfidf_scores)}

    # Sort the dictionary by TF-IDF score in descending order
    #sorted_word_tfidf = sorted(word_tfidf.items(), key=lambda x: x[1]["tfidf"], reverse=True)
    sorted_word_tfidf = dict(sorted(word_tfidf.items(), key=lambda x: x[1]["tfidf"], reverse=True))

    #print(">>>>>>>>>>@@@@@@@@@@@@@@@@>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #print(sorted_word_tfidf)
    # Print the top 10 words with their IDF and TF-IDF scores
   #== for word, scores in sorted_word_tfidf:
        #print(f"{word}: IDF - {scores['idf']}, TF-IDF - {scores['tfidf']}")
    return sorted_word_tfidf

#documents = ['test test2 test3 cefepim b c e f ', 'magnesium sulf magnesium sulf p26pkf potassium chloride replacement critical care oncolog metoprolol tartr metoprolol tartr morphine sulf potassium chloride replacement critical care oncolog potassium chloride replacement critical care oncolog potassium chloride replacement critical care oncolog potassium chloride replacement critical care oncolog cefepim cefepim p33k2x lidocaine 1 magnesium sulfate replacement critical care oncolog magnesium sulfate replacement critical care oncolog fentanyl citr fentanyl citr potassium chlorid potassium chlorid fentanyl citr quetiapine fumar quetiapine fumar p54tss magnesium sulf p851dg magnesium sulf p14csq metoprolol tartr p54tss metoprolol tartr insulin p28ev2 lidocaine 1 picc midline insert heparin calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium calcium gluconate sliding scale critical care ionized calcium potassium chlorid potassium chlorid magnesium sulf magnesium sulf magnesium sulf magnesium sulf magnesium sulf magnesium sulf morphine sulf ']

#generate_tfidf_vectorizer(documents)