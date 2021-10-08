#https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays
def mergeKArrays(self, arr, K):
    # code here
    from heapq import heapify, heappush, heappop

    heap = []
    a = []
    heapify(heap)
    x=0
    for i in range(K):
        for j in arr:
            heappush(heap,j[i])
    for i in range(K**2):
        a.append(heap[0])
        heappop(heap)
    return(a)
