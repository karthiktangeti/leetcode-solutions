class Solution(object):
    def countDays(self, days, meetings):
        meetings.sort()
        start,end = meetings[0]
        meetings_count = 0
        for s,e in meetings[1:]:
            if s <= end:
                end = max(e,end)
            else:
                meetings_count += end - start + 1
                start,end = s,e
        meetings_count += end - start + 1
        return days - meetings_count
