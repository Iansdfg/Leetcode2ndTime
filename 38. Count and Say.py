class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1):
            pre, count,temp = res[0], 0,''
            for pos in range(len(res)):
                if res[pos] == pre:
                    count += 1
                else:
                    temp += str(count)+pre
                    count = 1 
                    pre = res[pos]
            res = temp+ str(count)+res[pos]
        return res
