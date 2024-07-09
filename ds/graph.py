from collections import defaultdict

class Graph:
    """
    Graph class
    """
    def __init__(self, edges: list[(int, int)], bidirectional: bool = False):
        """
        Args:
            `edges`: list of edges
            `bidirectional`: whether to insert a back edge for each edge
        """
        self.g = defaultdict(list)

        for u, v in edges:
            self.g[u].add(v)
            if bidirectional:
                self.g[v].add(u)
        
        self.n = len(self.g)

        return self.g
    
    