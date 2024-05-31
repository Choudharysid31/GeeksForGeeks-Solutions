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
