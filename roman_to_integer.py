class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        conversion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0

        for i in range(len(s)):
            #print(i)
            if (i != len(s) - 1) and conversion.get(s[i]) < conversion.get(s[i+1]):
                result -= conversion.get(s[i])
            else:
                result += conversion.get(s[i])
        
        return result
    
    print(romanToInt('III'))
    print(romanToInt('LVIII'))
    print(romanToInt('MCMXCIV'))



