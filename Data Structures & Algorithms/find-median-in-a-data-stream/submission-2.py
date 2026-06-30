class MedianFinder:

    def __init__(self):
        # bigger num
        self.minHeap = []
        # smaller num
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)
            return
        
        if -self.maxHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            left = -heapq.heappop(self.maxHeap)
            right = heapq.heappop(self.minHeap)

            heapq.heappush(self.maxHeap, -right)
            heapq.heappush(self.minHeap, left)
        

    def findMedian(self) -> float:
        print(self.minHeap)
        print(self.maxHeap)
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        