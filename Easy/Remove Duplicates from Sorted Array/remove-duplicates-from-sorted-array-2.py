class Solution:
    def removeDuplicates(self, nums):
        nums = list(set(nums))
        return nums

# [1,1,2]

solution = Solution()
print(solution.removeDuplicates([1,1,2]))