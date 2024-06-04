class Solution:
    sum = 0
    def sum_of_first_n_numbers(self , N):
        if N == 0:
            return 
        self.sum += N
        self.sum_of_first_n_numbers(N-1)

s = Solution()
s.sum_of_first_n_numbers(5)
print(s.sum)
        