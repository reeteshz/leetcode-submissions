class Solution:
    def plusOne(self, digits):
        number = ""
        for x in digits:
            number += str(x)
        number = int(number)
        number += 1
        number = list(str(number))
        return number


solution = Solution()
print(solution.plusOne([0,2]))
# for i in range(len(digits)):