"""
Problem: Sort Vowels by Frequency
Platform: LeetCode
Link: Weekly Contest 499 - Q2
Approach: Frequency Count + First Occurrence + Replacing Vowels
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        freq = {}
        pos = {}

        for i, ch in enumerate(s):
            if ch in vowels:
                freq[ch] = freq.get(ch, 0) + 1
                if ch not in pos:
                    pos[ch] = i

        o = sorted(freq.keys(), key=lambda x: (-freq[x], pos[x]))

        sortedV = []

        for ch in o:
            sortedV.extend([ch] * freq[ch])

        s = list(s)
        idx = 0

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = sortedV[idx]
                idx += 1

        return "".join(s)


# Count frequency of each vowel and store its first occurrence index.
# Sort vowels by descending frequency and for equal frequency use first appearance.
# Build a separate correctly ordered vowel sequence using sorted frequencies.
# Replace only vowel positions in original string while keeping consonants unchanged.