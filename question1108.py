class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ""
        for i in address:
            if i == '.':
                result = result + "[.]"
            else:
                result = result + i
        return result
