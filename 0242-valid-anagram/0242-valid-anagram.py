class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = str(sorted(s))
        t = str(sorted(t))
        if t == s:
            return True
        else:
            return False