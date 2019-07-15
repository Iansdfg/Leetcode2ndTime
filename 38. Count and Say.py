class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            temp_res = ''
            pos = 0
            while pos<len(res):
                count = 1
                while pos<len(res)-1 and res[pos] == res[pos+1]:
                    pos +=1 
                    count+=1
                temp_res = temp_res + str(count)+res[pos]
                pos +=1
            res = temp_res
        return res
