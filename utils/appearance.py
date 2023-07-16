class Appearance:
    """
    Represents the appearance of a term in a given document, along with the
    frequency of appearances in the same one.
    """

    def __init__(self, doc_name, frequency, tag):
        #self.word = word
        self.docName = doc_name
        self.frequency = frequency
        self.tag = tag

    def to_dict(self):
        return {
            'docName': self.docName,
            'frequency': self.frequency,
            'tag':  self.tag
        }

    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)