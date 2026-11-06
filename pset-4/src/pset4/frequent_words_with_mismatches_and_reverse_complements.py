def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    
def reverseComplement(s: str) -> str:
        comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return "".join(comp[c] for c in reversed(s))

def _neighbors(pattern: str, d: int) -> set[str]:
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    result = set()
    for suffix in _neighbors(pattern[1:], d):
        if sum(a != b for a, b in zip(pattern[1:], suffix)) < d:
            for nucleotide in 'ACGT':
                result.add(nucleotide + suffix)
        else:
            result.add(pattern[0] + suffix) 
    return result

def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:
    counts = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        for word in _neighbors(kmer, d):
           counts[word] = counts.get(word, 0) + 1
        for word in _neighbors(reverseComplement(kmer), d):
              counts[word] = counts.get(word, 0) + 1
        if not counts:
            return set()
        best = max(counts.values())
        return {word for word, count in counts.items() if count == best}