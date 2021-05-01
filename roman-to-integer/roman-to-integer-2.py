class Solution:
    def romanToInt(self, s):
        i=0
        outputInt = 0
        decodeRoman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        while i < len(s):
            if s[i] in ["I", "X", "C"]:
                if i < len(s) - 1:
                    if s[i+1] in ["V", "X", "L", "C", "D", "M"] and s[i+1] != s[i] and decodeRoman[s[i]] < decodeRoman[s[i+1]]:
                        outputInt -= decodeRoman[s[i]]
                    else:
                        outputInt += decodeRoman[s[i]]
                else:
                    outputInt += decodeRoman[s[i]] 
            else:
                outputInt += decodeRoman[s[i]] 
            i += 1
        return outputInt

solution = Solution()
print(solution.romanToInt("DCXXI"))