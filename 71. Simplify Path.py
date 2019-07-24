class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for ele in path:
            if stack and ele  == '..':
                stack.pop()
            elif ele!='' and ele!='.' and ele  != '..':
                stack.append(ele)
        stack+=['']
        res = '/'.join(stack)
        res = '/'+res[:-1]
        return res
