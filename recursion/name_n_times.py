class Solution:
    n = 0
    def printName(self , name):
        if self.n == 5:
            return 
        print(name)
        self.n += 1
        self.printName(name)

s = Solution()
s.printName("Gurumurthy")

        