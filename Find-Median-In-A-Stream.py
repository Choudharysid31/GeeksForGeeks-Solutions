'''Given a data stream arr[] where integers are read sequentially, the task is to determine the median of the elements encountered so far after each new integer is read.

Input:  arr[] = [5, 15, 1, 3, 2, 8]
Output: [5.0, 10.0, 5.0, 4.0, 3.0, 4.0] 

Explanation: 
After reading 1st element of stream – 5 -> median = 5.0
After reading 2nd element of stream – 5, 15 -> median = (5+15)/2 = 10.0 
After reading 3rd element of stream – 5, 15, 1 -> median = 5.0
After reading 4th element of stream – 5, 15, 1, 3 ->  median = (3+5)/2 = 4.0
After reading 5th element of stream – 5, 15, 1, 3, 2 -> median = 3.0
After reading 6th element of stream – 5, 15, 1, 3, 2, 8 ->  median = (3+5)/2 = 4.0

Input: arr[] = [2, 2, 2, 2]
Output: [2.0, 2.0, 2.0, 2.0]
1 <= arr.size() <= 105
1 <= x <= 106 '''

class Solution:
    def getMedian(self, arr):
        import heapq
        minheap=[]
        maxheap=[]
        heapq.heapify(minheap)
        heapq.heapify(maxheap)
        ans=[]

        for i in arr:
            heapq.heappush(maxheap,-i)
            
            heapq.heappush(minheap,-heapq.heappop(maxheap))
                
            if len(minheap)>len(maxheap):
                heapq.heappush(maxheap,-heapq.heappop(minheap))

                
            if(len(minheap)+len(maxheap))%2:
                ans.append(-maxheap[0])
            else:
                ans.append((-maxheap[0]+minheap[0])/2)
                
        return ans
