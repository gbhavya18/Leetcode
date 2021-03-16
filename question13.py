class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        direc = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        result=0
        i = len(s)-1
        while(i>=0):
            print("s[i]:",s[i])
            if (((s[i] == 'V' or s[i] == 'X') and (s[i-1] == 'I'))or
            ((s[i] == 'L' or s[i] == 'C') and (s[i-1] == 'X'))or
            ((s[i] == 'D' or s[i] == 'M') and (s[i-1] == 'C'))) and i-1!=-1:
                temp = direc[s[i]]-direc[s[i-1]]
                print("temp:",temp)
                result+=temp
                print("result:",result)
                i-=1
            else:
                result+=direc[s[i]]
                print("result:",result)
            i-=1
        return result