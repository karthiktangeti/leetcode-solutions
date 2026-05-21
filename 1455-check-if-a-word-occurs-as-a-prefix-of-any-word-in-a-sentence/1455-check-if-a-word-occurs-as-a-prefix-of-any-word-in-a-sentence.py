class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        arr = sentence.split()
        for i in range(len(arr)):
            if arr[i].startswith(searchWord):
                return i + 1
        return -1

        