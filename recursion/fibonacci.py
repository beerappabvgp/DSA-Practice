class Solution:
    # using multiple recursion calls // learning recusrsion 
    def fib(self,n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

s = Solution()
print(s.fib(5))
