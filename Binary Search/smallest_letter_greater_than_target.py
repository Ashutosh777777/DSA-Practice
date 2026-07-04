class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        s = 0
        e = len(letters) - 1
        ans = -1

        while s <= e:
            m = (s + e) // 2

            if letters[m] > target:
                ans = m
                e = m - 1
            else:
                s = m + 1

        if ans == -1:
            return letters[0] 

        return letters[ans]