class Solution:
    def isValid(self, s):
        openingBrackets = ("(", "{", "[")
        closingBrackets = (")","}","]")
        bracketMatch = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []
        i = 0
        if len(s) == 1 or len(s) % 2 == 1:
            return False
        while i in range(len(s)) :
            if s[i] in openingBrackets:
                stack.append(s[i])
            elif s[i] in closingBrackets and len(stack) > 0:
                if bracketMatch[stack[len(stack)-1]] == s[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False
            i += 1
        return True if len(stack) == 0 else False

            

solution = Solution()
print(solution.isValid("[{{}]}"))
#([]{})

# "()"
# "()[]{}"
# "(]"
# "([)]"
# "{[]}"