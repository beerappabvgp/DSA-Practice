class Solution:
    def greater(self , rows):
        pattern = []
        number = 1
        for r in range(rows):
            pattern.append("*" * number)
            pattern.append("\n")
            number += 1
        print("".join(pattern[:len(pattern) - 1]))
        # second half
        # print(pattern)
        print("".join(pattern[::-1][3:]))

s = Solution()
s.greater(5)