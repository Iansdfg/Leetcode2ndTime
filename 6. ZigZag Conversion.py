class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        interval = 2*numRows-2
        res = ''
        num_of_row=0
        num_of_interval=0
        while len(res)<len(s):
            if interval*num_of_interval+num_of_row>len(s)-1:
                num_of_row+=1
                num_of_interval=0
            zig = interval * num_of_interval + num_of_row
            zag = interval * (num_of_interval+1)-num_of_row
            if num_of_row == 0 or num_of_row == numRows-1:
                res += s[zig]
            else:
                if zag > len(s) - 1:
                    res += s[zig]
                else:
                    res += s[zig]+s[zag]
            num_of_interval += 1
        return res
