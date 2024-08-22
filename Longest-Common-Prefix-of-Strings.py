'''Given an array of strings arr. Return the longest common prefix among each and every strings present in the array. If there's no prefix common in all the strings, return "-1".

Examples :
Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
Output: gee
Explanation: "gee" is the longest common prefix in all the given strings.
Input: arr[] = ["hello", "world"]
Output: -1
Explanation: There's no common prefix in the given strings.

Expected Time Complexity: O(n*min(|arri|))
Expected Space Complexity: O(min(|arri|))'''

class Solution:
    def longestCommonPrefix(self, arr):
        mini=arr[0]
        for i in arr:
            if len(i)<len(mini):
                mini=i
        ans=''
        flag=0
        for i in range(len(mini)):
            for j in range(len(arr)):
                if (arr[j][i]!=mini[i]):
                    flag=1
                    break
            if flag:
                break
            ans+=mini[i]
        if len(ans):
            return ans
        return -1
