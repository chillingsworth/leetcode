class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        forward = [i for i in str(x)]
        backward = [i for i in str(x)]
        backward.reverse()
        
        if forward == backward:
            return True
        else:
            return False
