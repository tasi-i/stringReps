def stringSpelledByGenomePath(patterns: list[str]) -> str:
    """Return the string spelled by the ordered genome path (BA3B)."""
    k = len(patterns[0])
    genome = ""

    # add the first letter of every k-mer (except the last one) to the genome
    for i in range(len(patterns)-1):
        genome += patterns[i][0]

    # add the length k-1 suffix of the last kmer to the genome
    genome += patterns[-1][-k:]

    return genome