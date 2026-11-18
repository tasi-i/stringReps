from matplotlib import text


def deBruijnFromString(k: int, text: str) -> list[list[str]]:

    
    """Return the de Bruijn graph of text as rows [source, destination] (BA3D).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    # TODO: Write your code here.
 
    edges = []
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        edges.append
    return edges


if __name__ == "__main__":
    import sys
    from collections import defaultdict

    k= int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    adjacency_list = defaultdict(list)
    for src, dst in deBruijnFromString(k, text):
        adjacency_list[src].append(dst)
    for src in sorted(adjacency_list):
        print(f"{src} -> {','.join(sorted(adjacency_list[src]))}")
        
    
    
