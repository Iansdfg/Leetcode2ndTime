class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return a or b
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1])+'0'
        elif a[-1] != b[-1] :
            return self.addBinary(a[:-1], b[:-1])+'1'
        else:
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1')+'0'
