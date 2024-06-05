class Solution:
    def triangle(self , rows):
        stars = 1
        spaces = rows * 2
        for r in range(rows):
            print(" " * spaces , end = "")
            for c in range(stars):
                print("*" , end = " ")
            stars += 2
            spaces -= 2
            print()

s = Solution()
s.triangle(5)