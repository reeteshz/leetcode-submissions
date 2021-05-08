class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        mid = int(x/2)
        while mid > 0:
            if mid * mid == x:
                return mid
            elif mid * mid > x: 
                mid = int(mid/2)
            else:
                break
        
        while x >= mid * mid:
            mid += 1

        return mid - 1
        
solution = Solution()
print(solution.mySqrt(2))