class Solution:
    def right_triangle(self , rows):
        num_to_add = 0
        res = ["1"]
        for r in range(1 , rows):
            print(res[0])
            res = [str(num_to_add) + " " + res[-1]]
            num_to_add = 1 if num_to_add == 0 else 0
        print(res[0])
        # for s in res:
        #     print(s)

s = Solution()
s.right_triangle(5)