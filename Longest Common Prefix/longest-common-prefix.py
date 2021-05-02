class Solution:
    def longestCommonPrefix(self, strs):
        j = 0
        i = 0
        prefix = ""
        while i < len(strs):
            if len(strs[i]) <= j:
                break
            elif strs[0][:j+1] == strs[i][:j+1]:
                if i >= len(strs) - 1:
                    i = 0
                    j += 1
                    prefix = strs[i][:j+1]
                else:
                    i += 1
            else:
                break
        return prefix[:j]

solution = Solution()
print(solution.longestCommonPrefix(["flo", "flight", "flower"]))