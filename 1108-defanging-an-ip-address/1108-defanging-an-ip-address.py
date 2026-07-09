class Solution(object):
    def defangIPaddr(self, address):
        res = list(address)
        for i in range(len(address)):
            if address[i] == ".":
                res[i] = "[.]"
        return "".join(res)
        