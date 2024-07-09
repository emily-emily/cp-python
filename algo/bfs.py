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
        curr, d = queue.pop(0)

        if target is not None and curr == target:
            return d, curr
        
        for i in graph[curr]:
            if not visited[i]:
                queue.append((i, d+1))
                visited[i] = True
    
    return d, curr