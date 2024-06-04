class Solution:
    # functional recursion where the function returns the answer to the subproblem from the function 
    def factorial(self , n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)
    
s = Solution()
print(s.factorial(5))