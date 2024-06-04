class Solution:
    # palindrome check using functional recursion 
    def palindrome_check(self , i , n , arr):
        if i >= n // 2:
            return True 
        if arr[i] != arr[n - i - 1]:
            print(i)
            return False
        return self.palindrome_check(i+1 , n , arr)

s = Solution()
print(s.palindrome_check(0 , 5 , "aagaa"))
        
        