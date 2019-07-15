class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1):
            temp, pre, cnt = '', res[0], 0
            for pos in range(len(res)):
                if res[pos] == pre:
                    cnt +=1
                else:
                    temp+= str(cnt)+pre
                    cnt = 1
                    pre = res[pos]
            res = temp+str(cnt)+pre
        return res
    
