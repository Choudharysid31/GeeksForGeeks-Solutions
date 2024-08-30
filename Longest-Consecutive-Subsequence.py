'''Given an array of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 
Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Expected Time Complexity: O(R), where R is the maximum integer in the array.
Expected Auxiliary Space: O(N).'''

    def findLongestConseqSubseq(self,arr, N):
        a=max(arr)
        b=min(arr)
        longest=0
        count=0
        dicti={}
        for i in arr:
            dicti[i]=1
        for i in range(b,a+1):
            if i not in dicti:
                longest=max(longest,count)
                count=0
            else:
                count+=1
        return max(longest,count)
