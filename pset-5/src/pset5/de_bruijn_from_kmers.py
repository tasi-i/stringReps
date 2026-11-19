def deBruijnFromKmers(patterns: list[str]) -> list[list[str]]:
    """Return the de Bruijn graph of the k-mers as rows [source, destination] (BA3E).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    # source is prefix, destination is suffix
    # each edge represents a k-mer
    
    graph :list[list[str]] = []
    # for every k-mer, decompose into prefix and suffix and add into the graph
    for kmer in patterns:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph.append([prefix,suffix])

    return graph

def rosalind_output_wrapper(graph):
    """
        Reformat deBruijn graph to the form Rosalind takes
    """
    p_to_s_graph = dict()

    # construct dictionary of prefix --> suffix list
    for edge in graph:
        if edge[0] in p_to_s_graph:
            p_to_s_graph[edge[0]].append(edge[1])
        else:
            p_to_s_graph[edge[0]] = [edge[1]]

    # adjacency list in the form: <prefix> -> <suffixes separated by commas>
        # print results
    for p in list(p_to_s_graph):
        s = ", ".join(p_to_s_graph[p])
        print(f"{p} -> {s}")