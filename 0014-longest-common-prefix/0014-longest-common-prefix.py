class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(len(prefix)):
            char = prefix[i]
            for s in strs[:]:
                if i >= len(s) or s[i] != char:
                    return prefix[:i]
        return prefix            
