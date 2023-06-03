class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num_parentheses = 0
        num_curly = 0
        num_brackets = 0
        valid = True

        #([)]
        for char in s:
            if char == '(':
                num_parentheses+=1
            elif char == ')':
                num_parentheses-=1
            elif char == '[':
                num_brackets+=1
            elif char == ']':
                num_brackets-=1
            elif char == '{':
                num_curly+=1
            elif char == '}':
                num_curly-=1
            if num_curly < 0 or num_brackets < 0 or num_parentheses < 0:
                valid = False
        if num_brackets!=0 or num_curly !=0 or num_parentheses !=0:
            valid = False
        return valid
            
        
            