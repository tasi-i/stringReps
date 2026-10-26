"""Rosalind BA1K: Generate the Frequency Array of a String."""


def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    symbol_to_num = {"A": 0, "C": 1, "G": 2, "T": 3}
    counts = [0] * (4**k)

    #compute index of first kmer
    index = 0
    for ch in text[:k]:
        index = 4 * index + symbol_to_num[ch]   
    counts[index] += 1

    #roll index forward onc character at a time
    mask = 4 ** k
    for i in range(k, len(text)):
        index = 4 *  symbol_to_num[text[i]] % mask 
        counts[index] += 1

    return counts

if __name__ == "__main__":
    import sys
    text = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    print(" ".join(map(str, frequencyArray(text, k))))