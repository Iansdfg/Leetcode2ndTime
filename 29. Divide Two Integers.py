class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if dividend*divisor>0 else -1
        dividend = abs(dividend); divisor = abs(divisor)
        if sign == 1 and dividend < divisor:return 0
        summ,res = 0,0
        while dividend>=divisor:
            summ = divisor
            count = 1
            while summ+summ<=dividend:
                summ+=summ
                count+=count
            dividend-=summ
            res+=count
        if sign*res>=2147483647:
            return 2147483647
        elif sign*res<=-2147483648:
            return -2147483648
        else:
            return sign*res
        
