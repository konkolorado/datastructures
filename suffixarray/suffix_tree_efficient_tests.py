from SuffixTreeEfficient import SuffixTreeEfficient

def test_compute_lcp_array():
    print("Testing compute lcp array... ", end='')
    sufftree = SuffixTreeEfficient("ABABAA")
    assert sufftree.lcp_array == [0, 1, 1, 3, 0, 2]
    print("Done")

def test_create_suffix_tree():
    print("Testing creating a suffix tree... ")
    sufftree = SuffixTreeEfficient("GTAGT")
    sufftree.create_suffix_tree()
    print("Done")


def main():
    test_compute_lcp_array()
    test_create_suffix_tree()


if __name__ == "__main__":
    main()
