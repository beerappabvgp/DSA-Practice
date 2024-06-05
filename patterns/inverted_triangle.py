class Solution:
    def inverted_triangle(self , rows):
        stars = (rows * 2) - 1
        spaces = 0
        for r in range(rows):
            print(" " * spaces, end = "")
            for c in range(stars):
                print("*" , end = " ")
            print()
            spaces += 2
            stars -= 2
    
s = Solution()
s.inverted_triangle(5)
