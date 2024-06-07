class Solution:
    def selection(self , arr):
        for i in range(len(arr)-1):
            min_idx = i
            for j in range(i+1 , len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
        return arr


s = Solution()
print(s.selection([4,1,2,7,5,0,300,10000,400,45,2,34,21,34,67,54,79,100 , 200]))

