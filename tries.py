# code by Group 7 (Khairina Atiqah)

class Node:
    def __init__(self):
        self.children = {} #children that the node points to
        self.endofword = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        ptr = self.root   # if ptr.children does not exist/ empty  
        
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
            # if ptr.children is exist/ not empty   
            ptr = ptr.children[letter]
        ptr.endofword = True
        
    def search(self, word):
        # if ptr.children does not exist/ empty
        ptr = self.root
        
        for letter in word:
            if letter not in ptr.children:
                return False
        #if ptr.children is exist/ not empty
            ptr = ptr.children[letter]
            
        # check the end of the word??
            return True

            
obj = Trie()
obj.insert("algorisfunalgoisgreat")
print(obj.search("algo"))
