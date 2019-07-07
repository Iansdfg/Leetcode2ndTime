class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'0': '',
               '1': '*',
               '2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz',
        }
        results = []
        for digit in digits:
            if results == []:
                for char in dic[digit]:
                    results.append(char)
            else:
                temp = []
                for result in results:
                    for ele in dic[digit]:
                        temp.append(result+ele)
                results = temp
        return results
            


        
        
