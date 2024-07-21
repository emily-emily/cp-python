from collections import defaultdict

class Graph:
    """
    Graph class
    """
    def __init__(self, edges: list[(int, int)], bidirectional: bool = False) -> None:
        """
        Args:
            `edges`: list of edges
            `bidirectional`: whether to insert a back edge for each edge
        """
        self.g = defaultdict(set)

        for u, v in edges:
            self.g[u].add(v)
            if bidirectional:
                self.g[v].add(u)
            if not v in self.g:
                self.g[v] = set()
        
        self.n = len(self.g)

    def topological_sort(self) -> list[int]:
        """
        Find topological sort of the graph

        Returns:
            List of vertices in topological ts.
            If the graph is not a DAG, returns None
        """
        ts = []
        visited = defaultdict(bool)
    
        def dfs(i):
            visited[i] = True
            for neighbor in self.g[i]:
                if not visited[neighbor]:
                    dfs(neighbor)
            ts.append(i)

        for i in self.g:
            if visited[i]:
                continue
            dfs(i)
        
        assert(len(ts) == self.n)

        ts.reverse()

        if self._check_ts(ts):
            return ts
        else:
            return None

    def _check_ts(self, ts: list[int]) -> bool:
        """
        Check if a topological sort is correct

        Args:
            `ts`: topological sort of the graph

        Returns:
            True if the topological sort is correct.
            False otherwise.
        """
        # map nodes to their indices in ts
        indices = {}
        for i, x in enumerate(ts):
            indices[x] = i

        # check each edge to make sure the topological sort is correct
        for i in self.g:
            for j in self.g[i]:
                if indices[i] > indices[j]:
                    return False
        return True
