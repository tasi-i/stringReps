"""Rosalind RNA: Transcribing DNA into RNA."""
# import regex library
import re

def transcribeRNA(text: str) -> str:
    """Return the RNA string corresponding to an uppercase DNA coding strand.

    Replace each T with U, retaining the order of the other nucleotides.
    """

    # use python regex library to find T's and substitute U's
    rna = re.sub("T", "U", text.upper())

    return rna