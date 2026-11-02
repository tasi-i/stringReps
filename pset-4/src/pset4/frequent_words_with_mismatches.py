class prefixNode:
    """Node class for nodes in a prefix tree including a prefix string, parent and children pointers"""
    # In this implementation the class for the prefix nodes is used to make the prefix expansion easier to think about
    # but isn't necessary since only the prefix string is used to generate neighbors
    def __init__(self, parent=None, str="",children=[]):
        self.parent = parent
        self.str = str
        self.children = children

def expandTree(node, pattern, current_mismatch_num, max_mismatch_num) -> list[str]:
    """ Recursively expand prefix tree until all neighbors of the pattern have been constructed, then return neighbors
        Neighbors are sequences of the same length as the pattern that have equal to or fewer mismatches than max_mismatch_num
    """
    # use the current node's string length to get the next position to expand (enumerate different nucleotides for)
    pos: int = len(node.str)

    # if the current string is the length of the pattern, then it is a neighbor, so return it
    if pos == len(pattern):
        # print(f"neighbor: {node.str}") # debugging
        return [node.str]

    # otherwise, recursively expand the prefix tree
    neighbors: list[str] = []
    # for every nucleotide that could go at the current position...
    for n in ["A","C","T","G"]:
        current: prefixNode = prefixNode(node, node.str+n)
        # if the nucleotide matches the next one in the pattern, then expand the subsequent nodes without increasing the mismatch count
        if pattern[pos] == n:
            neighbors += expandTree(current, pattern, current_mismatch_num, max_mismatch_num)
        # otherwise, if the mismatch number hasn't hit the max, expand the string with a mismatched nucleotide
        else:
            if current_mismatch_num < max_mismatch_num:
                neighbors += expandTree(current, pattern, current_mismatch_num+1, max_mismatch_num)
    return neighbors

def generateNeighbors(pattern: str, preTree: prefixNode, mismatch_num: int) -> list[str]:
    """Generate neighbors of given pattern (with mismatches <= mismatch_num) using the recursive tree expansion function"""
    return expandTree(preTree, pattern, 0, mismatch_num)

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    """ Find the most frequent words of length k in a piece of text, 
    allowing for d number of mismatches between the word and the instance in the text """

    # find frequency of each word with d or fewer mismatches
    freqMap: dict = dict()
    # for every position in the sequence, take the k-mer starting at that point
    for i in range(len(text)-k):
        # generate all its neighbors (k-mers with d or fewer mismatches)
            # neighborhood includes the k-mer itself since it has 0 mismatches with itself
        neighbors: list[str] = generateNeighbors(text[i:i+k], prefixNode(), d)
        # increment the frequency of all the neighbors 
        for neighbor in neighbors:
            if neighbor in freqMap:
                freqMap[neighbor] += 1
            else:
                freqMap[neighbor] = 1

    # find and return maximally frequent patterns
    freqWords: set[str] = set()
    max_count: int = max(freqMap.values())
    for word in freqMap:
        if freqMap[word] == max_count:
            freqWords.add(word)

    return freqWords