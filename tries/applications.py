from Trie import Trie
from SuffixTrie import SuffixTrie

def shortest_unique_substring(s1, s2):
    l_unique = unique_substrings_left(s1, s2)
    r_unique = unique_substrings_left(s2, s1)

    uniques = list(set(l_unique).union(set(r_unique)))
    uniques.sort(key=lambda item: (len(item), item))

    # Case that there are no unique substrings
    if len(uniques) == 0:
        print(uniques)
        return []
    print(uniques[0])
    return uniques[0]

def unique_substrings_left(l, r, sep='#'):
    """
    Finds the unique substrings that are in string l
    and not in string r. Returns them as a list
    """
    unique = []
    sf = SuffixTrie(l + sep + r)
    sf.compress_edge_labels()
    leaf_labels = sf.get_leaf_labels()
    inner_labels = sf.get_inner_labels()

    # Iterate outer nodes
    for label in leaf_labels:
        if sep in label and label[0] != sep:

            # Find and examine each possible path to the leaf node
            all_paths = sf.all_paths_to_label(label)
            for p in all_paths:
                p = p.split(',')
                p_last = len(p) - 1

                # Check if all nodes reachable from root contain sep symbol
                # If so, it means we only care about the label until the current
                # node
                if only_special_case_leaves(sf, int(p[0])):

                    # The last label in the path will be this labe, so stop before then
                    branch_label = sf.make_branch_label_from_path(p[:p_last], label)
                    if branch_label != "":
                        unique.append(branch_label)

                    sep_i = label.find(sep)
                    unique.append(branch_label + label[:sep_i])

                # Else, we care about the label for the branches until the current node
                # + the first symbol in the target label
                else:
                    branch_label = sf.make_branch_label_from_path(p[:p_last], label)
                    unique.append(branch_label + label[0])

    # If any inner nodes are special case, add their symbols along the path to them
    # to the unique list
    for label in inner_labels:
        for node in sf.get_all_nodes_with_label(label):
            if only_special_case_leaves(sf, node):
                path = sf.path_to(node, label).split(',')
                branch_label = sf.make_branch_label_from_path(path, label)
                unique.append(branch_label)

    return unique

def only_special_case_leaves(suff_trie, node):
    """
    Given a SuffixTrie and a node, checks if all leaves from this node are
    special case. Special case is that all leaves contain the special '#' symbol
    """
    leaves = suff_trie.get_leaf_labels_from_node(node)
    for l in leaves:
        if '#' not in l:
            return False
    return True

def main():
    shortest_unique_substring("ATGCGATGACCTGACTGA", "CTCAACGTATTGGCCAGA")
    shortest_unique_substring("CCAAGCTGCTAGAGG", "CATGCTGGGCTGGCT")
    shortest_unique_substring("AAAAAAAAAAAAAAAAAAAAA","TTTTTTTTTTTTTTTTTTTT")
    shortest_unique_substring("GODGOD","CAT")
    shortest_unique_substring("AA", "TT")
    shortest_unique_substring( "A","T")
    shortest_unique_substring("", "A")


if __name__ == '__main__':
    main()
