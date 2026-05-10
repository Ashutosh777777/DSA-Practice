"""
Problem: Count Word Occurrences
Platform: LeetCode
Link: 
Approach: String Parsing + Hash Map
Time Complexity: O(n + q)
Space Complexity: O(n)
"""

from collections import Counter

class Solution(object):
    def countWordOccurrences(self, chunks, queries):
        """
        :type chunks: List[str]
        :type queries: List[str]
        :rtype: List[int]
        """

        s = "".join(chunks)
        words = []
        cur = ""

        n = len(s)

        for i, ch in enumerate(s):

            if ch.islower():
                cur += ch

            elif ch == "-":
                if (
                    i > 0 and i < n - 1 and
                    s[i - 1].islower() and
                    s[i + 1].islower()
                ):
                    cur += ch

                else:
                    if cur:
                        words.append(cur)
                    cur = ""

            else:
                if cur:
                    words.append(cur)
                cur = ""

        if cur:
            words.append(cur)

        mp = Counter(words)

        return [mp[q] for q in queries]


# Join all chunks into one complete string.
# Build words character by character using lowercase letters.
# Keep '-' only when it is between two lowercase letters.
# Any other character breaks the current word.
# Count all extracted words using Counter.
# Return frequency of each query word.