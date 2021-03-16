class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stri = ""
        if s:
            for i in s:
                if i.lower() not in ['a','e','i','o','u']:
                    stri=stri+i
            return stri
        else:
            return stri