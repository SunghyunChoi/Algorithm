
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

in_string, search_string = map(int, r().split())
newTrie = Trie()
answer = 0
for _ in range(in_string):
    string = r().strip()
    newTrie.insert(string)
    
for _ in range(search_string):
    string = r().strip()
    if (newTrie.search(string)):
        answer += 1

print(answer)