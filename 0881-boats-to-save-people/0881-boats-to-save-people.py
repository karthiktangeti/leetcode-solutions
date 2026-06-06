class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        sum1 = 0
        count = 0
        l = 0
        r = len(people)- 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            count += 1
        return count

        