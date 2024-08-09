'''Given a string S, check if it is palindrome or not.
Example 1:
Input: S = "abba"
Output: 1
Explanation: S is a palindrome
Example 2:
Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome
Your Task:
You don't need to read input or print anything. Complete the function isPalindrome()which accepts string S and returns an integer value 1 or 0.
Expected Time Complexity: O(Length of S)
Expected Auxiliary Space: O(1)'''

class Solution:
	def isPalindrome(self, S):
		left=0
		right=len(S)-1
		while left<right:
		    if S[left]!=S[right]:
		        return 0
		    left+=1
		    right-=1
	    return 1
