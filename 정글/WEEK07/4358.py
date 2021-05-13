#생태학

import sys
from collections import defaultdict
r = sys.stdin.readline
answer = 0
class Node(object):
    def __init__(self,key, data=None):
        self.key = key
        self.data = data
        self.count = 0
        self.children = {}
        
class Trie(object):

    def __init__(self):
        self.head = Node(None)

    def insert(self, data):
        curr_node = self.head
        string = data.split(' ')
        for char in string:
            if char not in curr_node.children.keys():
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = data
        curr_node.count += 1
        return True

    def dfs(self):
        start = self.head
        
        def go(curr_node, n):
            key = curr_node.key
            if curr_node.data:
                global answer
                print("%s %.4f" % (curr_node.data, (curr_node.count / answer) * 100))
                sorted_children = sorted(curr_node.children.items())
            for child in sorted_children:
                go(child[1], n+1)
        sorted_children = sorted(start.children.items())
        for child in sorted_children:
            go(child[1], 0)

a = r().strip()
newTrie = Trie()
while(a != ''):
    newTrie.insert(a)
    a = r().strip()
    answer += 1

newTrie.dfs()