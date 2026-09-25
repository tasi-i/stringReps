
def FrequentWords(text: str, k: int) -> set[str]:
    if k > len(text) or not text:
        return set()

    substring_counts = {}
    max_count = 0

    for i in range(len(text) - k + 1):
        substring = text[i:i + k]
        count = PatternCount(text, substring)
        substring_counts[substring] = count
        if count > max_count:
            max_count = count

    most_frequent_substrings = {substring for substring, count in substring_counts.items() if count == max_count}


    return most_frequent_substrings
