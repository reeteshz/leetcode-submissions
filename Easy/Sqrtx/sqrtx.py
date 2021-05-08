class Solution:
    def mySqrt(self, x):
        i = 1
        while x >= i * i:
            i += 1
        
        return i - 1
        
solution = Solution()
print(solution.mySqrt(1))