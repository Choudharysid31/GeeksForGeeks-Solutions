'''Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.

Input: str1 = "heap", str2 = "pea"
Output: 3
Explanation: 2 deletions and 1 insertion.
p and h deleted from heap. Then, p is inserted at the beginning.
One thing to note, though p was required yet it was removed/deleted first from its position and then it is inserted to some other position. Thus, p contributes one to the deletion_count and one to the insertion_count.

Input : str1 = "geeksforgeeks", str2 = "geeks"
Output: 8
Explanation: 8 deletions, i.e. remove all characters of the string "forgeeks".

Expected Time Complexity: O(|str1|*|str2|)
Expected Space Complexity: O(|str1|*|str2|)'''

class Solution:
	def minOperations(self, s1, s2):
		dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
		for i in range(1,len(s1)+1):
		    for j in range(1,len(s2)+1):
		        if s1[i-1]==s2[j-1]:
		            dp[i][j]=1+dp[i-1][j-1]
		        else:
		            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	    return len(s1)+len(s2)-2*dp[-1][-1]
