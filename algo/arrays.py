import heapq

def topk(arr: list, k: int) -> list:
    """
    Args:
        arr: input array
        k: number of elements to return
    
    Returns:
        list: top k smallest elements, not sorted
    
    Runtime: O(n log k)
    
    Implementation: uses a maxheap to maintain the top k smallest elements
    """

    n = len(arr)
    heap = []
    for i in range(n):
        heapq.heappush(heap, -arr[i])
        if len(heap) > k:
            heapq.heappop(heap)
            
    return [-x for x in heap]
