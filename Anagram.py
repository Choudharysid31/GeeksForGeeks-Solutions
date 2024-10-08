''' Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other. Strings a and b can only contain lower case alphabets.
Note:- If the strings are anagrams you have to return True or else return False
|s| represents the length of string s.
Example 1:
Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same characters with same frequency. So, both are anagrams.
Example 2:
Input:a = allergy, b = allergic
Output: NO
Explanation: Characters in both the strings are not same, so they are not anagrams. 

Expected Time Complexity:O(|a|+|b|).
Expected Auxiliary Space: O(Number of distinct characters).'''

class Solution:
    def isAnagram(self,a,b):
        return sorted(list(a))==sorted(list(b))
