class Solution:

    def insertion(self , arr):
        for i in range(len(arr)):
            j = i 
            while (j and arr[j] < arr[j-1]):
                arr[j],arr[j-1] = arr[j-1],arr[j]
                j -= 1
        return arr

s = Solution()
print(s.insertion([1000,234,900,4,3,2,1]))
