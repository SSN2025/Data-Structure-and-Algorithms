import numpy as np
import heapq

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None



#s is th string of words
#ans is a map of character and code
def HuffmanCodes(s):
    freq = {}
    heap = []
    count=0

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1


    for char, f in freq.items():
        node = Node(char,f)
        heapq.heappush(heap,(freq,node))
        count+=1

    while len(heap) > 1 :
        freq1, _, left = heapq.heappop(heap)
        freq2 , _, right = heapq.heappop(heap)

        parent = Node(None,freq1+freq2)

        parent.left = left
        parent.right = right

        heapq.heappush(heap,(parent.freq,count,parent))
        count +=1

    root = heap[0][2]

    codes = {}
