import heapq

def mergeKLists(self, lists: List[ListNode]) -> ListNode:

    root  = result = ListNode(None)
    heap =[]
    

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, list[i]))


    while heap:

        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next

        if result.next:
            heapq.heappop(heap, (result.next.val, idx, result,next))

    return root.next

lists = [[1,4,5],[1,3,4],[2,6]]

print(mergeKLists(lists))