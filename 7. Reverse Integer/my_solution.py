class Solution:
    def reverse(self, x: int) -> int:           
        if x < 0:
            retval = int('-' + str(x)[::-1][:-1])
        elif 0 < x:
            retval = int(str(x)[::-1])
        else:
            retval = 0
            
        if -2**31 <= retval <= 2**31 - 1:
            return retval
        else:
            return 0