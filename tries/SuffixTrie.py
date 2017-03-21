from BaseTrie import BaseTrie

class SuffixTrie(BaseTrie):

    def __init__(self, text):
        self.text = text
        BaseTrie.__init__(self)

    def _build_trie(self):
        """ Builds a SuffixTree from the given text """
        self.text += self.terminal
        while len(self.text) != 0:
            self._add_branch(self.text)
            self.text = self.text[1:]

    def _add_branch(self, text):
        curr_id = self.root
        for i in range(0, len(text)):
            letter = text[i]
            if self._contains_symbol(curr_id, letter):
                curr_id = self._get_node_by_label(curr_id, letter)
            else:
                new_id = self._new_id()
                # NOTE find more efficient way of indicating end of branch,
                # other than creating an empty dict
                self._insert_new_node(new_id)
                self._set_node_by_label(curr_id, letter, new_id)
                curr_id = new_id

    def compress_edge_labels(self):
        """
        Makes the compact copy of the trie by merging nodes with singular children
        and updating edge values (A->T->C->$ becomes ATC$).
        """
        if hasattr(self, 'compressed_edges'):
            return self.compressed_edges

        self._merge_non_branching()
        self.compressed_edges = []
        for node in self._get_nodes():
            for label in self._get_labels(node):
                self.compressed_edges.append(label)
        return self.compressed_edges

    def _merge_non_branching(self):
        """
        Helper function for getting edge labels. Performs the actual merging
        """
        nodes = [0]
        #print(self.tree)
        while len(nodes) != 0:
            curr = nodes.pop()
            if curr == None:
                continue
            #print(curr, self._number_children(curr))
            if self._number_children(curr) == 0:
                continue

            # If this node has only 1 child, find all its parents and
            # update their children to be the children of this node,
            # while keeping track of and merging edge labels
            if self._number_children(curr) == 1:
                child_label = self._get_labels(curr)[0]
                child = self._get_node_by_label(curr, child_label)

                # Find the current node's parents and update its children
                for n in self.tree:
                    for n_label in self._get_labels(n):
                        if self._get_node_by_label(n, n_label) == curr:
                            self._link(n, child, n_label + child_label)
                            self._unlink(n, n_label)

                # Add the child to nodes to explore, delete the current node
                nodes.append(child)
                self._remove_node(curr)

            # If curr has more than one child, it will still be in the tree. Add
            # its children to nodes to explore
            if self._contains_node(curr):
                for l in self._get_labels(curr):
                    nodes.append(self._get_node_by_label(curr, l))

    def match(self, patterns):
        """
        Method that returns a list of patterns that were
        successfully found in the trie
        """
        matches = []
        for p in patterns:
            res = self._match_pattern(p)
            if res:
                matches.append(p)
        return matches

    def _match_pattern(self, p):
        text = p
        curr = self.root

        while len(text) > 0:
            symbol = text[0]


            # Reached a leaf label, check if remained of text
            # is a prefix of the leaf label
            if  not self._contains_symbol(curr, symbol):
                all_labels = self._get_labels(curr)
                text_len = len(text)
                for l in all_labels:
                    if text == l[:text_len]:
                        return True
                return False

            # Matched symbol on a branch, update text and curr
            if self._contains_symbol(curr, symbol):
                curr = self._get_node_by_label(curr, symbol)
                text = text[1:]

        # Reached end of text while searching on a branch
        return True

def main():
    #t = SuffixTrie("CCAAGCTGCTAGAGG#CATGCTGGGCTGGCT")
    t = SuffixTrie("CCC")

    print(t.compress_edge_labels())
    t.print_trie()
    print(t.match(["C", "CCC", "CC"]))

if __name__ == '__main__':
    main()
