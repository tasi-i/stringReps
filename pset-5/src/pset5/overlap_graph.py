from collections import defaultdict
def overlapGraph(patterns: list[str]) -> list[list[str]]:
    """Return the overlap graph as rows [source, destination] (BA3C).

    Each row contains one directed edge, with the source first.
    Row order does not matter.
    """

    unique = list(dict.fromkeys(patterns))

    #index every kmer by its prefix
    by_prefix = defaultdict(list)
    for p in unique:
        by_prefix[p[:-1]].append(p)

    edges = []
    for a in unique:
        for b in by_prefix[a[1:]]:
            edges.append([a, b])

    return edges