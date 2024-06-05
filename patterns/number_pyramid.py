class Solution:
    def pyramid(self , rows):
        numbers = rows
        for r in range(rows):
            for c in range(1 , numbers + 1):
                print(c , end = "")
            numbers -= 1
            print()

s = Solution()
s.pyramid(5)