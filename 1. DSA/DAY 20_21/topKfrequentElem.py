class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ha = {}
        for i in nums:
            if i not in ha:
                ha[i] = 1
            else:
                ha[i]+=1
        ha = sorted(ha.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
        s = []
        for (i,j) in ha[:k]:
            s.append(i)
        return s

##devs approach
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq,hp = Counter(nums),[]
        for el,count in freq.items():
            heapq.heappush(hp,(count,el))
            if len(hp)==k+1:
                heapq.heappop(heap)
        return [x[1] for x in hp]