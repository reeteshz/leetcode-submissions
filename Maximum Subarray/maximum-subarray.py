class Solution:
    def maxSubArray(self, nums):
        lenNums = len(nums)
        maxSum = sum(nums)
        i=0
        # pivot = 0
        j = lenNums
        while j != 1:
            i = 0
            j -= 1
            while i + j <= lenNums:
                # print(f">>>>>>> {nums[i: i+j]}")
                if maxSum < sum(nums[i: i+j]):
                    maxSum = sum(nums[i: i+j])
                    #pivot = i
                i += 1
        return maxSum

solution = Solution()
print(solution.maxSubArray([0,-3,-2,-3,-2,2,-3,0,1,-1]))