def hammingDistance(p: str, q: str) -> int:
    """Calculate Hamming distance (number of mismatches) between two equal length strings"""

    # if the strings are not equal lengths, raise exception
    if len(p) != len(q):
        raise Exception(f"Strings \"{p}\" and \"{q}\" are not the same length")

    # count the number of mismatches by incrementing counter if letters are not the same at a position
    dist: int = 0
    for i in range(len(p)):
        if p[i].upper() != q[i].upper():
            dist += 1
    return dist

print(hammingDistance("GGGCCGTTGGT",
"GGACCGTTGAC"))