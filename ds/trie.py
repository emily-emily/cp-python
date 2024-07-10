class Trie:
    """
    Trie data structure.
    """
    def __init__(self, valid: bool = False):
        """
        Initialize a Trie node.

        Args:
            `valid`: whether the current node represents a valid word
        """
        self.valid = valid
        self.next = dict()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            `word`: word to insert
        """
        # follow tree until we can no longer match any characters
        wn = len(word)
        cur = self
        i = 0
        while i < wn:
            if word[i] in cur.next:
                cur = cur.next[word[i]]
            else:
                cur.next[word[i]] = Trie()
                cur = cur.next[word[i]]
            i += 1
        # mark word as valid
        cur.valid = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        Args:
            `word`: word to search
        
        Returns:
            True if the word is found in the Trie.
            False otherwise.
        """
        wn = len(word)
        cur = self
        i = 0
        while i < wn:
            # check if we can match a character
            if word[i] in cur.next:
                cur = cur.next[word[i]]
                i += 1
            else:
                break
        return i == wn and cur.valid

    def prefixes(self, word: str) -> list[int]:
        """
        Find all prefixes of a word in the Trie.

        Args:
            `word`: word to search for prefixes
        
        Returns:
            List of indices of prefixes of the word in the Trie.
        """
        wn = len(word)
        cur = self
        i = 0
        prefixes = []
        while i < wn:
            if cur.valid:
                prefixes.append(i)

            if word[i] in cur.next:
                cur = cur.next[word[i]]
                i += 1
            else:
                break
        return prefixes
