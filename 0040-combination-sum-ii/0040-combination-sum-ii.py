class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        def backtrack(start,current,remaining):
            if remaining == 0:
                result.append(current[:])
                return
            
            for i in range(start,len(candidates)):
                if candidates[i] > remaining:
                    break
                if candidates[i] == candidates[i-1] and i > start:
                    continue

                current.append(candidates[i])
                backtrack(i+1,current, remaining - candidates[i])
                current.pop()
        
        backtrack(0,[],target)
        return result
                