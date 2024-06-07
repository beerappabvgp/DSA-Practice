class Solution:

    def bubble(self , arr):
        # swap adjacent elements by comparing them with each other 
        # get the largest element from the range and move it to the last
        n = len(arr)
        for i in range(n-1 , -1 , -1):
            swapped = False
            for j in range(0 , i - 1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    swapped = True
            if not swapped:
                return arr
        return arr

s = Solution()
print(s.bubble([4,3,2,100,6,8,1000]))

