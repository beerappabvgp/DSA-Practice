class Solution:
    def num2(self , rows):
        number = 1
        for r in range(rows):
            for c in range(1 , number+1):
                print(c , end = " ")
            number += 1
            print()

s = Solution()
s.num2(5)
