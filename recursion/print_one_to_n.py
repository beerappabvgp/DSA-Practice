class Solution:
    def print_lineraly(self , num , n):
        if num > n:
            return 
        print(num)
        self.print_lineraly(num + 1 , n)

s = Solution()
s.print_lineraly(1,40)



recursion 