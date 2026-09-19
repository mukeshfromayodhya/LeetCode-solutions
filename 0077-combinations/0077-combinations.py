class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        current = []
        ans = []
        start = 1
        def backtrack(current, start):
            if len(current) == k:
                ans.append(current[:])
                return 
            for i in range(start,n+1):
                current.append(i)
                backtrack(current,i+1)
                current.pop()
        backtrack([],1)     
        return ans 
            



            