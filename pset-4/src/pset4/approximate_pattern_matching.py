def approximatePatternMatching(pattern: str, text: str, d: int) -> list[int]:
    k = len(pattern)
    positions = []
    for i in range(len(text) - k + 1):
        mismatches = 0
        for a, b in zip(pattern, text[i:i + k]):
            if a != b:
                mismatches += 1
                if mismatches > d:
                    break
        if mismatches <= d:
            positions.append(i)
    return positions