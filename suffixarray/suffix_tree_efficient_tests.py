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

def main():
    test_compute_lcp_array()
    test_create_suffix_tree()


if __name__ == "__main__":
    main()
