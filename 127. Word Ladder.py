class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord,1))
        while bfs:
            curr,lenth = bfs.popleft()
            if curr == endWord:return lenth
            for i in range(len(curr)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new = curr[:i]+c+curr[i+1:]
                    if new in wordset and new != curr:
                        wordset.remove(new)
                        bfs.append((new, lenth+1))
        return 0
