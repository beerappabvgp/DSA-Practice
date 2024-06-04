class Solution:
    def print_N(self , N):
        if N == 0:
            return 
        print(N)
        self.print_N(N - 1)

s = Solution()
s.print_N(40)