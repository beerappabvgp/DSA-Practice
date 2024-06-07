class Solution:
    def selection(self , arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i] , arr[j] = arr[j],arr[i]
        return arr


s = Solution()
print(s.selection([4,1,2,7,5,0,45,2,34,21,34,67,54,79,100]))

