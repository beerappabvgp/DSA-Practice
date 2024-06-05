class Solution:
    def num(self,rows):
        number = 1
        for r in range(rows):
            for c in range(number):
                print(number , end = " ")
            number += 1
            print()

s = Solution()
s.num(5)