import numpy as np
import heapq as hq
from collections import Counter as cntr
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq



#s is th string of words
#ans is a map of character and code
def tree(s):
    fr = cntr(s)
    heap = [Node(ch, f) for ch, f in fr.items()]
    hq.heapify(heap)
    ans = {}
    while(len(heap) >  1):
        l = hq.heappop(heap)
        r = hq.heappop(heap)

        nxt = Node(None,l.freq + r.freq)
        nxt.left = l
        nxt.right = r
        hq.heappush(heap,nxt)
    return heap[0] if heap else None
    ##################################################333
            
def HuffCodes(node,curr="",temp = None):
    if temp is None:
        temp = {}

    if node is not None:
        if node.char is not None:
            temp[node.char] = curr
        HuffCodes(node.left, curr+"0",temp)
        HuffCodes(node.right, curr+"1",temp)

    return temp


root = tree("ieqyfuqioeiuqegtuoyweqoiuriuq3ewwgifgru3iyfgruy3gfru2qky3tr")
codes = HuffCodes(root)
print(codes)
