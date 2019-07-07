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
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
                
#         wordset = set(wordList)
#         if endWord not in wordset:
#             return 0
#         beginset = {beginWord}
#         endset = {endWord}
#         ladder_len = 2
#         while beginset:
#             if len(beginset)>len(endset):
#                 beginset,endset = endset,beginset
#             nextset = set()
#             for word in beginset:
#                 for i in range(len(word)):
#                     for c in "abcdefghijklmnopqrstuvwxyz":
#                         new = word[:i]+c+word[i+1:]
#                         if new in endset:
#                             return ladder_len
#                         if new in wordset:
#                             nextset.add(new)
#                             wordset.remove(new)
#             beginset = nextset
#             ladder_len+=1
#         return 0
                    
