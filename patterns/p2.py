# * 
# * *
# * * *

class Solution:
    def p2(self , rows):
        star = 1
        for r in range(rows):
            for c in range(star):
                print("*" , end = " ")
            star += 1
            print()

s = Solution()
s.p2(5)
