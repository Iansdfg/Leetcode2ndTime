class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cycle = 2*numRows-2
        if numRows==1:return s
        row_num, cyc_num = 0,0
        res = ''
        while len(res)<len(s):
            if cyc_num*cycle+row_num>len(s)-1:
                cyc_num = 0
                row_num += 1
            zig = cyc_num*cycle+row_num
            zag = (cyc_num+1)*cycle-row_num
            if row_num == 0 or row_num == numRows-1:
                res+=s[zig]
            else:
                if zag>len(s)-1:
                    res+=s[zig]
                else:
                    res+=s[zig]+s[zag]
            cyc_num+=1
        return res
