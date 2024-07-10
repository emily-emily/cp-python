import math

class SegmentTree:
    """
    Segment tree for range queries and point updates.

    Operations:
        - `update(i, val)`: update the value at index `i` to `val` in O(log n)
        - `query(l, r)`: query the range [l, r] in O(log n)
    
    Assumes the operation runs in O(1).

    The root of the tree is at index 1, and the array elements are at indices [p, p+n-1].
    """
    def __init__(self, arr: list[any], op: callable):
        """
        Initialize the segment tree.

        Args:
            `arr`: input array
            `op`: binary operation to perform on the ranges
        """
        self.n = len(arr)
        # smallest power of 2 greater than or equal to n
        self.p = 2 ** math.ceil(math.log2(self.n))
        self.op = op
        self.tree = [None] * (2 * self.p)
        self.tree[self.p:self.p+self.n] = arr
        self.build()

    def build(self) -> None:
        """
        Helper function to build the segment tree.
        """
        for i in range(self.p-1, 0, -1):
            if self.tree[2*i] is not None and self.tree[2*i+1] is not None:
                self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])

    def query(self, l: int, r: int) -> any:
        """
        Query the range [l, r], 0-indexed and inclusive.

        Args:
            `l`: left index
            `r`: right index
        
        Returns:
            The result of the query.
        """
        return self._query_helper(l, r, 1, 0, self.p-1)

    def _query_helper(self, l: int, r: int, i: int, tl: int, tr: int) -> any:
        """
        Helper function for the query operation.

        Args:
            `l`: left index of search range
            `r`: right index of search range
            `i`: current node
            `tl`: left bound of current node
            `tr`: right bound of current node
        """
        if l > r:
            return None
        if l == tl and r == tr or tl == tr:
            return self.tree[i]
        assert(i < 2 * self.p)
        tm = (tl + tr) // 2
        leftres = self._query_helper(l, min(r, tm), 2*i, tl, tm)
        rightres = self._query_helper(max(l, tm+1), r, 2*i+1, tm+1, tr)
        
        if leftres is None:
            return rightres
        if rightres is None:
            return leftres
        return self.op(leftres, rightres)

    def update(self, i: int, val: any) -> None:
        """
        Update the value at index `i` to `val`.

        Args:
            `i`: index to update
            `val`: new value
        """
        # start at leaf node and move up
        i += self.p
        self.tree[i] = val
        while i > 1:
            i //= 2
            if self.tree[2*i] is None:
                self.tree[i] = self.tree[2*i+1]
            elif self.tree[2*i+1] is None:
                self.tree[i] = self.tree[2*i]
            else:
                self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])
