# arr = list(map(int , input().split()))
# def get_freq_map(arr):
#     freq = {}
#     for ele in arr:
#         freq[ele] = freq.get(ele , 0) + 1
#     return freq

# freq = get_freq_map(arr)
# print(freq)


# class Solution:

#     num = 1
#     def printNo(self , N):
#         if self.num == 3: return 
#         print(self.num)
#         self.num += 1
#         self.printNo(N)

class Solution:    
    #Complete this function
    num = 1
    def printNos(self,N):
        # nonlocal num
        if self.num == N:
            return 
        print(self.num)
        self.num += 1
        self.printNos(N)

s = Solution()
s.printNos(3)
print(s.num)