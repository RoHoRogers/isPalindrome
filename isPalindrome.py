class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        s = str(x)
        
        if s[0] == '-':
            return False        
        if len(s) == 1:
            return True
        
        for i in range(len(s)-1):
            if s[i] != s[len(s)-1-i]:
                return False
            
        return True
