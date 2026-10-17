import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = [-n for n in nums]
        heapq.heapify(self.max_heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        k_largest = heapq.nsmallest(self.k,self.max_heap)
        return -k_largest[len(k_largest)-1]

        
