"""Rosalind BA1C: Find the Reverse Complement of a String."""

def reverseComplement(text: str) -> str:
    """Return the reverse complement of an uppercase DNA string.

    A pairs with T, and C pairs with G. Return the complementary
    nucleotides in reverse order.
    """

    # reverse string
    reverse = text[::-1].upper()
    # swap A --> T, C --> G, vice versa
    reverse_comp = ""
    for i in range(len(text)):
        if reverse[i] == "A":
            reverse_comp = reverse_comp + "T"
        elif reverse[i] == "T":
            reverse_comp = reverse_comp + "A"
        elif reverse[i] == "C":
            reverse_comp = reverse_comp + "G"
        elif reverse[i] == "G":
            reverse_comp = reverse_comp + "C"
        else:
            raise Exception("Non-canonical base in DNA string")


    return reverse_comp
