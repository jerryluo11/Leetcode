class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for string in strs:
            updated_prefix = ''
            for i in range(len(string)):
                if (i < len(prefix)) and string[i] == prefix[i]:
                    updated_prefix += string[i]
                else:
                    break
            prefix = updated_prefix

        return prefix