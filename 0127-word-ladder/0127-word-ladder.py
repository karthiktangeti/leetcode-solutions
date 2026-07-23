from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        queue = deque()
        queue.append((beginWord,1))
        while queue:
            curr,level = queue.popleft()
            if curr == endWord:
                return level
            for i in range(len(curr)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if curr[i] == ch:
                        continue
                    new_word  = curr[:i] + ch + curr[i + 1:]
                    if new_word in wordset:
                        queue.append((new_word,level + 1))
                        wordset.remove(new_word)
        return 0