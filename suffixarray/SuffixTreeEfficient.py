"""
Efficient construction of a SuffixTrie for a string
"""

from SuffixArrayEfficient import SuffixArrayEfficient

class SuffixTreeEfficient(object):
    def __init__(self, text, terminal="$"):
        self.text = text + terminal
        self.suffix_array = SuffixArrayEfficient(text).build_suffix_array()
        self.lcp_array = self._compute_lcp_array()

    def __str__(self):
        return "Text:" + self.text + "\nSuffixArray:" + str(self.suffix_array)

    def _invert_suffix_array(self, order):
        pos = [0] * len(order)
        for i in range(len(order)):
            pos[order[i]] = i
        return pos

    def _lcp_of_suffixes(self, S, i, j, equal):
        lcp = max(0, equal)
        while i + lcp < len(S) and j + lcp < len(S):
            if S[i+lcp] == S[j+lcp]:
                lcp += 1
            else:
                break
        return lcp

    def _compute_lcp_array(self):
        """
        Computes the least common prefixes among all suffixes. For each
        number at location i in the array, this represents the number of
        common characters in a prefix between suffix at position i and
        suffix at position i + 1.
        For example
        - suffix array = [$, a$, aa$, bb$, bbb$]
        - lcp array = [0, 1, 0, 2]
        """
        lcp_arr = [0] * (len(self.text) - 1)
        lcp = 0
        pos_in_order = self._invert_suffix_array(self.suffix_array)
        suffix = self.suffix_array[0]
        for i in range(len(self.text)):
            order_index = pos_in_order[suffix]
            if order_index == len(self.text) - 1:
                lcp = 0
                suffix = (suffix + 1) % len(self.text)
                continue
            next_suffix = self.suffix_array[order_index + 1]
            lcp = self._lcp_of_suffixes(self.text, suffix, next_suffix, lcp-1)
            lcp_arr[order_index] = lcp
            suffix = (suffix + 1) % len(self.text)
        return lcp_arr
