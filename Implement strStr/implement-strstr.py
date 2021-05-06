class Solution:
    def strStr(self, haystack, needle):
        lenNeedle = len(needle)
        lenHaystack = len(haystack)
        if lenNeedle == 0:
            return 0
        if lenHaystack == 0 or lenHaystack < lenNeedle:
            return -1
        for i in range(len(haystack)):
            if i + lenNeedle >= lenHaystack and haystack == needle:
                return 0
            elif haystack[i:i+lenNeedle:1] == needle:
                return i
            else:
                i +=i
        return -1
       




solution = Solution()
# print(solution.strStr("hello","ll"))
# print(solution.strStr("aaaaa","bba"))
# print(solution.strStr("",""))
# print(solution.strStr("mwscxsd","d"))
print(solution.strStr("x","dwdkwdn"))