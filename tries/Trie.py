from BaseTrie import BaseTrie

class Trie(BaseTrie):
    def __init__(self, patterns):
        self.patterns = patterns
        BaseTrie.__init__(self)

    def _build_trie(self):
        """ Builds a trie from a list of provided patterns """
        for p in self.patterns:
            p += self.terminal
            curr_id = self.root
            for i in range(0, len(p)):
                letter = p[i]
                if letter in self._get_labels(curr_id):
                    curr_id = self._get_node_by_label(curr_id, letter)
                else:
                    new_id = self._new_id()
                    self._insert_new_node(new_id)
                    self._set_node_by_label(curr_id, letter, new_id)
                    curr_id = new_id

    def match(self, text):
        """
        Will iterate through the text, trying to match it against any
        of the stores patterns. Returns a list containing the indices
        of the text where a match was found and a list of the patterns
        which were successfully matched
        """
        p, points, patterns = 0, [], []
        while len(text) != 0:
            matched = self._match_pattern_prefix(text, patterns)
            if matched:
                points.append(p)
            text = text[1:]
            p += 1
        return points, patterns

    def _match_pattern_prefix(self, text, patterns):
        pos = 0
        curr = self.root
        path = []

        while True:
            # Reached a leaf, indicating matched pattern
            if self.terminal in self._get_labels(curr):
                patterns.append( ''.join(path))
                return True

            # Check bounds before updating current symbol
            if pos >= len(text):
                return False

            symbol = text[pos]
            # Found a non-matching symbol
            if not self._contains_symbol(curr, symbol):
                return False

            if self._contains_symbol(curr, symbol):
                path.append(symbol)
                curr = self._get_node_by_label(curr, symbol)
                pos += 1

def main():
    t = Trie(["AA"])
    print(t.tree)
    t.print_trie()
    print(t.match("AAA"))

if __name__ == '__main__':
    main()
# TODO make sure no duplicate code in BaseTrie methods
