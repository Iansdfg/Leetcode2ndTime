class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:return s
        cycle = 2*numRows-2
        res = ''
        cycle_num = 0
        row_num = 0
        while len(res)<len(s):
            if cycle_num*cycle+row_num>len(s) - 1:
                cycle_num = 0
                row_num += 1
            zig = cycle*cycle_num+row_num
            zag = cycle*(cycle_num+1)-row_num
            if row_num == 0 or row_num == numRows-1:
                res+=s[zig]
            else:
                if zag > len(s)-1:
                    res+=s[zig]
                else:
                    res+=s[zig]+s[zag]
            cycle_num += 1
        return res 
