import bisect
class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.array, num)
        ## simply a efficeint way of append then sort in array


    def findMedian(self) -> float:
        if len(self.array)==0:
            return 0
        if len(self.array)==1:
            return self.array[0]
        l = len(self.array)
        return (self.array[l//2] + self.array[(l-1)//2])/2 

1 2 3 4 5
 index 2 2
 1 2 3 4 5 6
index 3 2 
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()