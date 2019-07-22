class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        return str(int(''.join([str(digit) for digit in digits ]))+1)
