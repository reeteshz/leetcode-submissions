class Solution:
    def longestCommonPrefix(self, strs):
        j = 0
        i = 0
        prefix = ""
        while i in range(len(strs)) and strs[i].find(strs[0][:j+1]) == 0 and j < len(strs[i]):
            if len(strs) == 1:
                return strs[0]
            i += 1
            if len(strs) - 1 == i and strs[i].find(strs[0][:j+1]) == 0:
                prefix = strs[0][:j+1]
                j += 1
                i = 0
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["ab", "ab", "abc"]))