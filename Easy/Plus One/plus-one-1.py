class Solution:
    def plusOne(self, digits):
        carry = 0
        for i in range(len(digits), 0, -1):
            if i == len(digits):
                digits[i - 1] += 1
            if carry == 1:
                digits[i - 1] += 1
                carry = 0
            if digits[i - 1] > 9:
                digits[i - 1] = 0
                carry = 1
        if carry == 1:
            digits.insert(0,1)    
        return digits

solution = Solution()
print(solution.plusOne([9,1,2]))