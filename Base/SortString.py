class Solution:
    def sortString(self, s: str) -> str:
        # code here
        new = ""
        for c in sorted(s):
            new+=c
        return new