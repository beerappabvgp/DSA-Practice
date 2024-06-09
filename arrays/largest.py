class Solution:
    def largest(self , arr):
        large = arr[0]
        for n in arr:
            if n > large:
                large = n
        return large
    
s = Solution()
print(s.largest([1,2,4,68,6666]))