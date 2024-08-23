import heapq

def topk(arr: list, k: int) -> list:
    """
    Args:
        arr: input array
        k: number of elements to return
    
    Returns:
        list: top k smallest elements
    """

    n = len(arr)
    heap = []
    for i in range(n):
        heapq.heappush(heap, arr[i])
    ans = []
    for _ in range(k):
        ans.append(heapq.heappop(heap)[1])
    return ans