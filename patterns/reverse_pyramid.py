class Solution:
    def pyramid(self , rows):
        stars = rows
        for r in range(rows):
            for c in range(stars):
                print("*",end = "")
            stars -= 1
            print()

s = Solution()
s.pyramid(5)