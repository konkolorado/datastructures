from SuffixTreeEfficient import SuffixTreeEfficient

def test_compute_lcp_array():
    print("Testing compute lcp array... ", end='')
    sufftree = SuffixTreeEfficient("ABABAA")
    assert sufftree.lcp_array == [0, 1, 1, 3, 0, 2]
    print("Done")


def main():
    test_compute_lcp_array()


if __name__ == "__main__":
    main()
