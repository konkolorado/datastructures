"""
Node definition for use with the SuffixTreeEfficient class
"""

class SuffixTreeNode(object):
    def __init__(self, parent, string_depth, edge_start, edge_end):
        self.parent = parent
        self.children = {}
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end

    def __str__(self):
        return str(self.string_depth) + "Children: " + str(self.children) + \
            str(self.edge_start) + str(self.edge_end)
