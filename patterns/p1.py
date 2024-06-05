# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

class Solution:
    def p1(self,rows):
        for r in range(rows):
            for c in range(rows):
                print("*" , end = " ")
            print()

s = Solution()
s.p1(10)