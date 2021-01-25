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
            if(curr_node.data):
                return False
            if char not in curr_node.children.keys():
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        if(curr_node.children):
            return False
        curr_node.data = string
        return True

test_case = int(r())
for _ in range(test_case):
    input_num = int(r())
    newTrie = Trie()
    flag = True
    for _ in range(input_num):
        if(newTrie.insert(r().strip())):
            continue
        else:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")