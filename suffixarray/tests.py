from SuffixArray import SuffixArray

def test_suffix_array():
    print("Testing suffix array creation...", end="")
    assert SuffixArray("GAC").suffix_indices == (3,1,2,0)
    assert SuffixArray("GAGAGAGA").suffix_indices == (8,7,5,3,1,6,4,2,0)
    assert SuffixArray("AACGATAGCGGTAGA").suffix_indices == \
        (15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5)
    print("All tests passed")

def main():
    test_suffix_array()

if __name__ == '__main__':
    main()
