class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        word_sets =  [set(word) for word in words]
        max_product = 0
        for i in range(n):
            for j in range(i + 1,n):
                if word_sets[i].isdisjoint(word_sets[j]):
                    max_product = max(max_product,len(words[i]) * len(words[j]))
        return max_product