class Solution:
    def full_pyramid(self , rows):
        # half pyramid
        pattern = []
        spaces = rows * 2
        number = 1
        for r in range(rows):
            s = " " * spaces
            st = "* " * number
            pattern.append(s+st)
            pattern.append("\n")
            spaces -= 2
            number += 2
        print("".join(pattern[:len(pattern) - 1]))

        # inverted half pyramid
        # print(pattern)
        print("".join(pattern[::-1][1:]))



s = Solution()
s.full_pyramid(5)