class Solution:

    # functional recursion
    def reverse_array(self , arr):
        if len(arr) == 1:
            return [arr[0]]
        return self.reverse_array(arr[1:]) + [arr[0]]

    # using two pointers
    arr = [1,2,3,100]
    def reverse_two_pointers(self , l , r):
        if l >= r:
            return 
        self.arr[l] , self.arr[r] = self.arr[r] , self.arr[l]
        self.reverse_two_pointers(l + 1 , r - 1)
    
    # using single pointer pattern 

    def reverse_single_pointer(self , i , n):
        if n - i - 1 <= i:
            return 
        self.arr[i] , self.arr[n-i-1] = self.arr[n-i-1] , self.arr[i]
        self.reverse_single_pointer(i + 1 , n) 
            
s = Solution()
print(s.reverse_array([1,2,3,4,5,6]))
# print(s.arr)
# s.reverse_two_pointers(0,len(s.arr) - 1)
# print("After reversing ... " , s.arr)
print("using single pointer...")
s.reverse_single_pointer(0,len(s.arr))
print(s.arr)