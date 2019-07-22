class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12:
            return []
        res = []
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, path, res):
        if len(s)<=0 and len(path)==4:
            res.append(".".join(path))
            return 
        for i in range(1,4):
            # 能否满足在最多4个3位数字组成
            if len(s)//3 + len(path) > 4:
                return
            if i>len(s): continue
            num = int(s[:i])
            if num<=255 and str(num) == s[:i]:
                self.dfs(s[i:], path+[s[:i]], res)
        
