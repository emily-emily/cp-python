class DisjointSet():
    """
    Disjoint Set (Union Find) data structure.
    """
    def __init__(self, n: int):
        """
        Initialize a Disjoint Set of n elements.
        """
        self.roots = [i for i in range(n)]
        self.num_sets = n
    
    def find(self, a: int) -> int:
        """
        Find the root of the set of a.

        Returns:
            The root of the set of a.
        """
        if self.roots[a] == a: return a
        else:
            # update to directly point to root
            self.roots[a] = self.find(self.roots[a])
            return self.roots[a]
    
    def union(self, a: int, b: int) -> bool:
        """
        Join two sets.

        Returns:
            True if the sets are joined successfully.
            False if the sets are already the same.
        """
        a, b = self.find(a), self.find(b)
        if a == b: return False
        self.roots[a] = b
        self.num_sets -= 1
        return True
    