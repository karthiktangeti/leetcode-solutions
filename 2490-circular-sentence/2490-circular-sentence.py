class Solution(object):
    def isCircularSentence(self, sentence):
        if sentence[0] != sentence[-1]:
            return False
        arr = list(sentence.split(" "))
        for i in range(len(arr) - 1):
            if arr[i][-1] != arr[i +1][0]:
                return False
        return True
        