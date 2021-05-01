class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if (nums[i] > target and target > 0 ) or (nums[i] < target and target < 0) :
                break
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i,j]

solution = Solution()
print(solution.twoSum([-1,-2,-3,-4,-5],-8))

