"""Find the most frequent words of a given length in text."""

from .pattern_count import PatternCount


def FrequentWords(text: str, k: int) -> set[str]:
    """Return all length-k substrings with the highest occurrence count.

    Count overlapping, case-sensitive matches and include every tie once.
    Assume k is a positive integer. Return an empty set if k exceeds the
    length of text or text is empty.

    Example:
        FrequentWords("ATAT", 2) returns {"AT"}.
        FrequentWords("ATGC", 2) returns {"AT", "TG", "GC"}.

    PatternCount is already imported above. You can call
    PatternCount(text, pattern) directly in your implementation.
    """
    # TODO: Implement this function.
    raise NotImplementedError("Implement FrequentWords")


def FrequentWords(text: str, k: int) -> set[str]:
    if k > len(text) or not text:
        return set()

    most_frequent_substrings = {substring for substring, count in substring_counts.items() if count == max_count}
    
    substring_counts = {}
    max_count = 0

    for i in range(len(text) - k + 1):
        substring = text[i:i + k]
        count = PatternCount(text, substring)
        substring_counts[substring] = count
        if count > max_count:
            max_count = count


    return most_frequent_substrings
