class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10
            x = int(x)
        print(x,revertedNumber)
        return x == revertedNumber or x == int(revertedNumber/10)
        
solution = Solution()
print(solution.isPalindrome(121))