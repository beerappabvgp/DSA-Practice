class Solution:
    def selection(self , arr):
        for i in range(len(arr)):
            mini = i
            for j in range(i + 1, len(arr)):
                if arr[mini] > arr[j]:
                    mini = j
            arr[mini] , arr[i] = arr[i],arr[mini]
        return arr


s = Solution()
print(s.selection([4,1,2,7,5,0,300,400,45,2,34,21,34,67,54,79,100 , 200]))

