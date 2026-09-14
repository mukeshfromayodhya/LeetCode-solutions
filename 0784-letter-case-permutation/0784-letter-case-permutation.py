class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, current_s):
            if i == len(s):
                ans.append(current_s)
                return
            char = s[i]
            if char.isdigit():
                current_s = current_s + char
                i += 1
                backtrack(i,current_s)
                return
            else:
                backtrack(i+1,current_s + char.lower())
                backtrack(i+1,current_s +char.upper())
        backtrack(0,"")        
        return ans

