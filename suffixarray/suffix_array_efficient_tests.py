"""
Contains source code for testing the implementation of
the efficient construction algorithm for a suffix array
"""

from SuffixArrayEfficient import SuffixArrayEfficient

def test_custom_alpha():
    print("Testing custom alphabet... ", end='')

    assert SuffixArrayEfficient("", custom_alpha=False).alpha == \
        "$ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert SuffixArrayEfficient("").alpha == \
        "$ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("Done")

def test_sort_characters():
    print("Testing sorting characters... ", end='')
    assert SuffixArrayEfficient("ABABAA")._sort_characters() == [6,0,2,4,5,1,3]
    print("Done")

def test_compute_character_classes():
    print("Testing comput character classes... ", end='')
    suff = SuffixArrayEfficient("ABABAA")
    order = suff._sort_characters()
    classes = suff._compute_character_classes(order)
    assert classes == [1,2,1,2,1,1,0]
    print("Done")

def test_update_classes():
    print("Testing updating classes... ", end='')
    suff = SuffixArrayEfficient("ABABAA")
    classes = [1,2,1,2,1,1,0]
    new_order = [6,5,4,0,2,1,3]
    new_classes = suff._update_classes(new_order, classes, 1)
    assert new_classes == [3,4,3,4,2,1,0]
    print("Done")

def test_build_suffix_arrray():
    print("Testing build suffix array... ", end='')

    assert SuffixArrayEfficient("ABABAA").build_suffix_array() == \
        [6, 5, 4, 2, 0, 3, 1]
    assert SuffixArrayEfficient("AAA").build_suffix_array() == [3,2,1,0]
    assert SuffixArrayEfficient("GAC").build_suffix_array() == [3,1,2,0]
    assert SuffixArrayEfficient("GAGAGAGA").build_suffix_array() == \
        [8,7,5,3,1,6,4,2,0]
    assert SuffixArrayEfficient("AACGATAGCGGTAGA").build_suffix_array() == \
        [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]

    print("Done")

def main():
    test_custom_alpha()
    test_sort_characters()
    test_compute_character_classes()
    test_update_classes()
    test_build_suffix_arrray()


if __name__ == '__main__':
    main()
