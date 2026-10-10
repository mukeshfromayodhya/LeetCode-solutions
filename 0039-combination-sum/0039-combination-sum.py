class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def backtrack(start,current,remaining):
            if remaining == 0:
                result.append(current[:])
                return
            
            for i in range(start,len(candidates)):
                if candidates[i] > remaining:
                    continue

                current.append(candidates[i])
                backtrack(i,current,remaining - candidates[i])
                current.pop()
        backtrack(0,[], target)
        return result