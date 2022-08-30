import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = front = ListNode()
        heap, sequence = [], 0
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, sequence, head))
                sequence += 1
        while heap:
            _, _, head = heapq.heappop(heap)
            front.next, head = head, head.next
            front = front.next
            if head:
                sequence += 1
                heapq.heappush(heap, (head.val, sequence, head))
        return root.next