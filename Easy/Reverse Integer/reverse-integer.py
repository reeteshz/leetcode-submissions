class Solution:
    def reverse(self, x):
        if x >= 0:
            xstr = str(x)
            xstr = xstr[::-1]
            xstr = int(xstr)
            return xstr if xstr <= (2 ** 31 - 1) else 0
        else:
            xstr = str(x * -1)
            xstr = xstr[::-1]
            xstr = int(xstr) * -1
            return xstr if xstr >= (-2 ** 31) else 0

solution = Solution()
print(solution.reverse(1534236469))