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
        node = self.head
        answer = 0
        
        for idx, char in enumerate(string):
            if char == '?':
                for child in node.children.values():
                    answer += search(child, string[idx+1:])
            elif char not in node.children.keys():
                return False
            node = node.children[char]
        if curr_node.data:
            return answer + 1
        return answer

new_Trie = Trie()
answer_list = []
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
for word in words:
    new_Trie.insert(word)

for query in queries:
    answer = 0
    answer = new_Trie.search(new_Trie.head, query)
    answer_list.append(answer)

print(answer_list)

