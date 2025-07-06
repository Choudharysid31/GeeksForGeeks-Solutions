'''You are given two integer arrays a[] and b[] of equal size. A sum combination is formed by adding one element from a[] and one from b[], using each index pair (i, j) at most once. Return the top k maximum sum combinations, sorted in non-increasing order.

Input: a[] = [3, 2], b[] = [1, 4], k = 2
Output: [7, 6]
Explanation: Possible sums: 3 + 1 = 4, 3 + 4 = 7, 2 + 1 = 3, 2 + 4 = 6, Top 2 sums are 7 and 6.

Input: a[] = [1, 4, 2, 3], b[] = [2, 5, 1, 6], k = 3
Output: [10, 9, 9]
Explanation: The top 3 maximum possible sums are : 4 + 6 = 10, 3 + 6 = 9, and 4 + 5 = 9

1 ≤ a.size() = b.size() ≤ 105
1 ≤ k ≤ a.size()
1 ≤ a[i], b[i] ≤ 104'''

class Solution:
    def topKSumPairs(self, a, b, k):

        import heapq
        a.sort(reverse=True)
        b.sort(reverse=True)
        n=len(a)
        
        h=[]
        heapq.heappush(h,[-(a[0]+b[0]),0,0])
        visited={(0,0)}
        
        ans=[]
        
        while len(ans)<k and h:
            curr_sum,left,right=heapq.heappop(h)
            ans.append(-curr_sum)
            if left+1<n and (left+1,right) not in visited:
                heapq.heappush(h,[-(a[left+1]+b[right]),left+1,right])
                visited.add((left+1,right))
            if right+1<n and (left,right+1) not in visited:
                heapq.heappush(h,[-(a[left]+b[right+1]),left,right+1])
                visited.add((left,right+1))
                
        return ans

