from SuffixTreeEfficient import SuffixTreeEfficient

def test_compute_lcp_array():
    print("Testing compute lcp array... ", end='')
    sufftree = SuffixTreeEfficient("ABABAA")
    assert sufftree.lcp_array == [0, 1, 1, 3, 0, 2]
    print("Done")

def test_create_suffix_tree():
    print("Testing creating a suffix tree... ", end='')

    st = SuffixTreeEfficient("AAA")
    st.create_suffix_tree()
    rep = repr(st.display_tree())
    assert rep == repr('$\nA\n\t$\n\tA\n\t\t$\n\t\tA')

    st = SuffixTreeEfficient("A")
    st.create_suffix_tree()
    rep = repr(st.display_tree())
    assert rep == repr('$\nA')

    st = SuffixTreeEfficient("GTAGT")
    st.create_suffix_tree()
    rep = repr(st.display_tree())
    assert rep == repr('$\nAGT$\nGT\n\t$\n\tAGT$\nT\n\t$\n\tAGT')

    print("Done")

def test_find_pattern():
    print("Testing find pattern... ", end='')


    st = SuffixTreeEfficient("GTAGT")
    st.create_suffix_tree()
    assert st.find_pattern("B") == []
    assert st.find_pattern("GTAGT") == [0]
    assert st.find_pattern("$") == [5]
    assert st.find_pattern("TAGT") == [1]
    assert st.find_pattern("AGT") == [2]
    assert st.find_pattern("GTA") == [0]
    assert st.find_pattern("TAG") == [1]
    assert st.find_pattern("GT") == [3, 0]
    assert st.find_pattern("AG") == [2]
    assert st.find_pattern("G") == [3, 0]
    assert st.find_pattern("A") == [2]
    assert st.find_pattern("T") == [4, 1]

    st = SuffixTreeEfficient("AAA")
    st.create_suffix_tree()
    assert st.find_pattern("AAA") == [0]
    assert st.find_pattern("B") == []
    assert st.find_pattern("A") == [2, 1, 0]
    assert st.find_pattern("AA") == [1, 0]

    st = SuffixTreeEfficient("A")
    st.create_suffix_tree()
    assert st.find_pattern("A") == [0]
    assert st.find_pattern("") == []
    assert st.find_pattern("B") == []
    assert st.find_pattern("AA") == []

    print("Done")

def main():
    test_compute_lcp_array()
    test_create_suffix_tree()
    test_find_pattern()

if __name__ == "__main__":
    main()
