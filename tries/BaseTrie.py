from abc import ABC, abstractmethod

import json

class BaseTrie(ABC):

    def __init__(self, terminal='$'):
        self.id = 0
        self.terminal = terminal
        self.root = self.id
        self.tree = {self.root: {} }
        self._build_trie()

    def __str__(self):
        return str(self.tree)

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if self.iter <= self.id:
            temp = self.iter
        else:
            raise StopIteration
        self.iter += 1
        return temp

    @abstractmethod
    def _build_trie(self):
        pass

    @abstractmethod
    def match(self):
        pass

    def get_all_nodes_with_label(self, label):
        targets = []
        all_nodes = self._get_nodes()
        for node in all_nodes:
            if self._contains_symbol(node, label):
                targets.append(node)
        return targets

    def _get_nodes(self):
        return self.tree.keys()

    def _contains_symbol(self, curr, symbol):
        return symbol in self.tree[curr]

    def print_trie(self):
        self._print_trie_helper([self.root], "")

    def _print_trie_helper(self, history, space):
        curr = history.pop(0)
        for l in self.tree[curr]:
            print(space + str(curr) + "->" + str(self.tree[curr][l]) + ":" + l)
            history.append(self.tree[curr][l])
            self._print_trie_helper(history, space +"\t")

    def all_paths_to_label(self, label):
        ps_to_l = []
        paths = [""]
        nodes = [self.root]
        while len(nodes) != 0:
            curr_node = nodes.pop(0)
            curr_path = paths.pop(0)

            for l in self._get_labels(curr_node):
                next_node = self._get_node_by_label(curr_node, l)
                nodes.append(next_node)
                if curr_path == "":
                    paths.append(str(next_node))
                else:
                    paths.append(curr_path + "," + str(next_node))

                if l == label:
                    ps_to_l.append( paths[-1])
        return ps_to_l

    def _get_labels(self, node):
        return list(self.tree[node])

    def _get_node_label(self, src, dest):
        for label in self._get_labels(src):
            if self._get_node_by_label(src, label) == dest:
                return label

    def _new_id(self):
        self.id += 1
        return self.id

    def path_to(self, node, label):
        p_to_l = []
        paths = [""]
        nodes = [self.root]

        while len(nodes) != 0:
            curr_node = nodes.pop()
            curr_path = paths.pop()

            for l in self._get_labels(curr_node):
                next_node = self._get_node_by_label(curr_node, l)
                nodes.append(next_node)
                if next_node == node:
                    if curr_path == "":
                        return str(next_node)
                    else:
                        return curr_path + "," + str(next_node)
                elif curr_path == "":
                    paths.append(str(next_node))
                else:
                    paths.append(curr_path + "," + str(next_node))
        return None

    def _get_node_by_label(self, node, label):
        """ Returns the child for a given node's label """
        return self.tree[node][label]

    def make_branch_label_from_path(self, path, target_label):
        label = ""
        curr = self.root

        for p in path:
            if p != 'None':
                new_node_label = self._get_node_label(curr, int(p))
                label += new_node_label
                curr = self._get_node_by_label(curr, new_node_label)
        return label

    def get_leaf_labels(self):
        leaf_labels = []
        to_explore = [self.root]
        while len(to_explore) != 0:
            curr_node = to_explore.pop(0)
            for label in self._get_labels(curr_node):
                next_node = self._get_node_by_label(curr_node, label)
                if self._number_children(next_node) == 0:
                    leaf_labels.append(label)
                else:
                    to_explore.append(next_node)

        return leaf_labels

    def _number_children(self, node):
        return len(self.tree[node])

    def get_leaf_labels_from_node(self, node):
        leaf_nodes = []
        to_explore = [node]
        while len(to_explore) != 0:
            curr_node = to_explore.pop(0)

            for label in self._get_labels(curr_node):
                next_node = self._get_node_by_label(curr_node, label)
                if self._number_children(next_node) == 0:
                    leaf_nodes.append(label)
                else:
                    to_explore.append(next_node)

        return leaf_nodes

    def get_inner_labels(self):
        inner_labels = []
        to_explore = [self.root]
        while len(to_explore) != 0:
            curr_node = to_explore.pop(0)
            for label in self._get_labels(curr_node):
                next_node = self._get_node_by_label(curr_node, label)
                if self._number_children(next_node) != 0:
                    inner_labels.append(label)
                    to_explore.append(next_node)
        return inner_labels

    def _insert_new_node(self, node):
        """ Creates a new int:{} entry in the trie """
        self.tree[node] = dict()

    def _contains_node(self, node):
        return node in self.tree

    def _set_node_by_label(self, node, label, newchild):
        """ Sets the child for a node's label """
        self.tree[node][label] = newchild

    def _remove_node(self, node):
        del self.tree[node]

    def _unlink(self, node, label):
        """ Removes the child of the node and its associated label """
        del self.tree[node][label]

    def _link(self, parent, grandchild, new_label):
        """ Adds a new_label to a node and links it to another node """
        self.tree[parent][new_label] = grandchild
