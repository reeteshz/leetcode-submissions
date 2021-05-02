class Solution:
    def removeDuplicates(self, nums):
        index = 1
        for i in range(len(nums)):
            if nums[i] not in nums[0: index]:
                carry = nums[index]
                nums[index] = nums[i]
                nums[i] = carry
                index += 1
                # nums[i] = nums[index] + nums[i]
                # nums[index] = nums[i] - nums[index]
                # nums[i] = nums[index] - nums[i]
        return index if len(nums) != 0 else 0

# [1,1,2]

solution = Solution()
print(solution.removeDuplicates([]))