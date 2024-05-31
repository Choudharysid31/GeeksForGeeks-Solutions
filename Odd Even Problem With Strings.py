'''Given a string s of lowercase English characters, find out whether the summation of x and y is even or odd, where x is the count of distinct characters that occupy 
even positions in English alphabets and have even frequency,
y is the count of distinct characters which occupy odd positions in English alphabets and have odd frequency.
Note: Positive means greater than zero.
Example 1:
Input: 
s = "abbbcc"
Output: 
ODD
Explanation: 
x = 0 and y = 1 so (x + y) is ODD. 'a' occupies 1st place(odd) in english alphabets and its frequency is odd(1), 'b' occupies 2nd place(even) but its frequency is odd(3) 
so it doesn't get counted and 'c' occupies 3rd place(odd) but its frequency is even(2) so it also doesn't get counted.'''



class Solution:
    def oddEven(self, s : str) -> str:
        x=0
        y=0
        s1=set(list(s))
        for i in s1:
            if s.count(i)%2==0 and (ord(i)-ord('a')+1)%2==0:
                x=x+1
            elif s.count(i)%2==1 and (ord(i)-ord('a')+1)%2==1:
                y=y+1
        if (x+y)%2:
            return "ODD"
        return "EVEN"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = (input())
        obj = Solution()
        res = obj.oddEven(s)
        print(res)
