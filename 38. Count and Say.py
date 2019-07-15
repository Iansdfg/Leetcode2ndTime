class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in xrange(n-1):
            new_res, pre, count = '', res[0], 0
            for pos in xrange(len(res)):
                if res[pos] == pre:
                    count += 1
                else:
                    new_res += str(count) + pre
                    count = 1
                    pre = res[pos]
            res = new_res + str(count) + pre
        return res
