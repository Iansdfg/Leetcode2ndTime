class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        if sign == 1 and divisor>dividend:return 0
        summ,res = 0,0
        while divisor<=dividend:
            summ = divisor
            count = 1
            while summ + summ<=dividend:
                summ+=summ
                count+=count
            dividend -= summ
            res+=count
        if -2**31<sign*res<2**31-1:
            return sign*res
        elif -2**31>=sign*res:
            return -2**31
        elif sign*res>=2**31-1:
            return 2**31-1
