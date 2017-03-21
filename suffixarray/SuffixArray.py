#python3

class SuffixArray(object):
    """
    Suffix arrays: a memory efficient alternative to suffix trees
    self.array contains the sorted suffixes
    self.suffix_indices contains the index of occurence for its
        corresponding suffix in the original text
    """
    def __init__(self, text):
        if not text.endswith('$'):
            text += "$"
        self.text = text
        self._create_array()

    def _create_array(self):
        self.array = []
        self.suffix_indices = []

        for i in range(len(self.text)-1, -1, -1):
            self.array.append(self.text[i:])
            self.suffix_indices.append(i)
        sorted_data = sorted(zip(self.array, self.suffix_indices))
        self.array, self.suffix_indices = zip(*sorted_data)
