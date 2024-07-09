from ..ds.graph import Graph

def bfs(graph: Graph, source: int, target: int = None) -> tuple[int, int]:
    """
    BFS traversal of a graph.

    Args:
        `graph`: Graph
        `source`: source node
        `target`: target node. If None, assumes the target is the furthest node from the source.
    
    Returns:
        The distance of the target node from the source node.
        The target node itself.
    """
    visited = [False for _ in graph.n]
    visited[source] = True

    queue = [(source, 0)]

    while queue:
        cur, d = queue.pop(0)

        if target is not None and cur == target:
            return d, cur
        
        for i in graph[cur]:
            if not visited[i]:
                queue.append((i, d+1))
                visited[i] = True
    
    return d, cur