class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char1 in stones:
            if char1 == char1 in jewels:
                count += 1
        return count