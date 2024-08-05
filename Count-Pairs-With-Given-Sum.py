'''Given an array arr, and an integer k, find the number of pairs of elements in the array whose sum is k.
Examples:
Input: k = 6, arr[] = [1, 5, 7, 1]
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.
Input: k = 2, arr[] = [1, 1, 1, 1]
Output: 6
Explanation: Each 1 will produce sum 2 with any 1.'''

    def getPairsCount(self, arr, sum):
        hash={}
        count=0
        for i in arr:
            if sum-i in hash:
                count+=hash[sum-i]
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        return count
