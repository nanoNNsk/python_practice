class Solution:
    def reverse(self, x: int):
        s = str(x)
        if s=='0':
            return 0 
        if s[0] == '-':
            s = '-' + s[:0:-1]  
        else:
            s = s[::-1]
        s = s.lstrip('0')
        s = int(s)
        if s > 2**31-1 or s < -2**31:
            return 0
        return s

sol = Solution()
x = int(input())
result = sol.reverse(x)
print(result)