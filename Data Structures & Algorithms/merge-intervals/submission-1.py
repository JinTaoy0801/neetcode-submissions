class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda interval: interval[0])


        prev, curr = 0,1
        ret = []
        while curr < len(intervals):
            if intervals[curr][0] <= intervals[prev][1]:
                temp = []
                first = min(intervals[curr][0], intervals[prev][0])
                second = max(intervals[curr][1], intervals[prev][1])

                while curr < len(intervals) and intervals[curr][0] <= second:
                    second = max(intervals[curr][1], second)
                    curr+=1

                temp.append(first)
                temp.append(second)
                ret.append(temp)
            else:
                ret.append(intervals[prev])
            prev = curr

        return ret
