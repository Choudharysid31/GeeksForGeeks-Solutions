'''Given an array of strings words[]. Find the longest string in words[] such that every prefix of it is also present in the array words[]. If multiple strings have the same maximum length, return the lexicographically smallest one.

Input: words[] = ["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]
Output: pros
Explanation: "pros" is the longest word with all prefixes ("p", "pr", "pro", "pros") present in the array words[].

Input: words[] = ["ab", "a", "abc", "abd"]
Output: abc
Explanation: Both "abc" and "abd" has all the prefixes in words[]. Since, "abc" is lexicographically smaller than "abd", so the output is "abc".

1 ≤ words.length() ≤ 103
1 ≤ words[i].length ≤ 103'''

class Solution():
    def longestString(self, words):
        words.sort()
        words.sort(reverse=True, key=lambda x:len(x))
        seti=set(words)

        for word in words:
            flag=True
            stri=""
            for c in word:
                stri+=c
                if stri not in seti:
                    flag=False
                    break
            if flag:
                return word
        return ""
