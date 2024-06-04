# without using parameters

class Solution:
    def sum_without_parameters(self , N):
        if N == 0:
            return 0
        return N + self.sum_without_parameters(N-1)

s = Solution()
print(s.sum_without_parameters(3))