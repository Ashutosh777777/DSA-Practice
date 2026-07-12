class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        h1, m1, s1 = map(int, startTime.split(":"))
        h2, m2, s2 = map(int, endTime.split(":"))
        return (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1)