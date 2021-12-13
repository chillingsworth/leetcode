class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) >= numRows:
            rows = [[] for x in range(numRows)]
        else:
            rows = [[] for x in range(len(s))]
        goingdown=True
        row=0
        for j,c in enumerate(s):
            if row <= len(rows):
                rows[row].append(c)
            if numRows != 1:
                if goingdown==True:
                    row+=1
                else:
                    row-=1
            if row==numRows-1:
                goingdown=False
            if row==0:
                goingdown=True
        ret = ""
        for r in rows:
            for x in r:
                ret+=x
        return ret