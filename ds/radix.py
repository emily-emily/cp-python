from ..str.misc import prefix

class Radix:
    """
    Radix tree, the optimized Trie.

    Properties:
    - Each node in the Radix tree has a prefix and points to the next node(s) with the next character in the word.
    - Tree is pruned when nodes are deleted to remove invalid leaves and combine nodes when possible.
    """
    def __init__(self, prefix = "", valid: bool = False) -> None:
        self.prefix = prefix
        self.valid = valid
        self.next = dict()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Radix tree.

        Args:
            `word`: word to insert
        """
        common_prefix, node_left, word_left = prefix(self.prefix, word)

        # case 1: word == prefix
        # mark node as valid
        if self.prefix == word:
            self.valid = True
        
        # case 2: word shorter than prefix or prefix doesn't match fully
        elif len(node_left):
            # split the current node
            cur_suffix = Radix(prefix=node_left, valid=True)
            cur_suffix.next = self.next
            self.prefix = common_prefix
            self.valid = False
            self.next = {node_left[0]: cur_suffix}

            # insert the remaining word
            if word_left:
                word_suffix = Radix(prefix=word_left, valid=True)
                self.next[word_left[0]] = word_suffix
            else:
                self.valid = True

        # case 3: no children with prefix of word
        # create new node with word
        elif word_left[0] not in self.next:
            self.next[word_left[0]] = Radix(prefix=word_left, valid=True)

        # follow prefix
        else:
            assert(node_left == "")
            self.next[word_left[0]].insert(word_left)

    def find(self, word: str) -> bool:
        """
        Find a word in the Radix tree.

        Args:
            `word`: word to find

        Returns:
            True if the word is found, False otherwise
        """
        if self.prefix == word:
            return self.valid
        _, node_left, word_left = prefix(self.prefix, word)

        if node_left:
            return False
        
        # follow prefix
        next_node = self.next.get(word_left[0], None)
        if next_node:
            return next_node.find(word_left)
        return False
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the Radix tree.

        Args:
            `word`: word to delete

        Every node in the radix tree is at least one of the following:
        - valid word
        - has 2+ children
        """
        if self.prefix == word:
            self.valid = False
            return True

        _, node_left, word_left = prefix(self.prefix, word)

        if node_left:
            return False
        
        next_node = self.next.get(word_left[0], None)

        if next_node:
            next_node.delete(word_left)
            # remove invalid leaf
            if not next_node.valid and not next_node.next:
                del self.next[word_left[0]]
            # merge with next node if self has only one child and is not valid
            # do not merge the root node
            if self.prefix != "" and not self.valid and len(self.next) == 1:
                next_key = list(self.next.keys())[0]
                next_node = self.next[next_key]
                self.prefix += next_key + next_node.prefix
                self.valid = next_node.valid
                self.next = next_node.next
            return True
        return False

    def startsWith(self, word: str) -> bool:
        """
        Determines if any word in the Radix tree starts with the given prefix.

        Implemented for LeetCode problem 208.
        """
        _, node_left, word_left = prefix(self.prefix, word)

        if word_left == "":
            return True
        if node_left:
            return False
        next_node = self.next.get(word_left[0], None)
        if next_node:
            return next_node.startsWith(word_left)
        return False
    