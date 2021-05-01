class Solution:
    def longestCommonPrefix(self, strs):
        i = 0
        prefix = strs[0]
        while i in range(len(strs)):
            if len(strs) == 1:
                return strs[0]
            while( strs[i].find(prefix) != 0):
                prefix = prefix[0: len(prefix)-1]
                if len(prefix) == 0:
                    return ""
            i += 1
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["flow", "flight", "flower"]))