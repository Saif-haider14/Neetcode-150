class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for  i  in nums :
            freq[i] = freq.get(i , 0)+1

        heap = [(count , num) for num , count in freq.items()] 

        heapq.heapify(heap)

        for i in range (len(heap) - k):
            heapq.heappop(heap)


        return [num for count , num in heap]      
        
        