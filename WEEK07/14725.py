##개미굴 탐색

import sys
from collections import defaultdict
r = sys.stdin.readline

class Node(object):
    def __init__(self,key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        
class Trie(object):

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children.keys():
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string
        return True
    
    def search(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children.keys():
                return False
            curr_node = curr_node.children[char]
        if curr_node.data :
            return True

    def dfs(self):
        start = self.head

        def go(curr_node, n):
            key = curr_node.key
            output = n*"--" + key
            print(output)
            sorted_children = sorted(curr_node.children.items())
            for child in sorted_children:
                go(child[1], n+1)
        sorted_children = sorted(start.children.items())
        for child in sorted_children:
            go(child[1], 0)

in_string = int(r())
newTrie = Trie()

for _ in range(in_string):
    string = r().strip().split()[1:]
    newTrie.insert(string)
    
newTrie.dfs()
