class Solution:
    def romanToInt(self, s):
        s = list(s)
        i=0
        outputInt = 0
        while i < len(s):
            if s[i] == 'I':
                if i < len(s) - 1 :
                    if s[i+1] == 'V' or s[i+1] == 'X':
                        outputInt -= 1
                    else:
                        outputInt += 1
                else:
                    outputInt += 1
            elif s[i] == 'X':
                if i < len(s) - 1:
                    if s[i+1] == 'L' or s[i+1] == 'C':
                        outputInt -= 10
                    else:
                        outputInt += 10
                else:
                    outputInt += 10
            elif s[i] == 'C':
                if i < len(s) - 1:
                    if s[i+1] == 'D' or s[i+1] == 'M':
                        outputInt -= 100
                    else:
                        outputInt += 100
                else:
                    outputInt += 100
            elif s[i]== 'M':
                outputInt += 1000
            elif s[i]== 'D':
                outputInt += 500
            elif s[i]== 'L':
                outputInt += 50
            elif s[i]== 'V':
                outputInt += 5
            i += 1
        return outputInt
    
        


solution = Solution()
print(solution.romanToInt('C'))