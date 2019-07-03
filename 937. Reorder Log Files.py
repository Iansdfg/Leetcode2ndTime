class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digit = []
        for log in logs:
            logsplit = log.split(" ")

            if logsplit[1].isdigit():
                digit.append(log)
            else:
                letter.append((" ".join(logsplit[1:]),logsplit[0]))
        # print(sorted(letter), digit)
        return [ele[1]+ ' ' +ele[0] for ele in sorted(letter)]+digit
        
