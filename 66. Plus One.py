# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """

#         return str(int(''.join([str(digit) for digit in digits ]))+1)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(digits)-1, -1, -1):
            digits[i]+=1
            if digits[i]<10:
                return digits
            else:
                digits[i] = 0
        return [1]+ digits
                
                
