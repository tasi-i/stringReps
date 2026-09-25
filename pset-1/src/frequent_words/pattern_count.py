def PatternCount(text: str, pattern: str) -> int:
  
    if len(pattern) > len(text) or not text:
        return 0

    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1

    return count