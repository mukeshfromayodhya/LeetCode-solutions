class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for i in range(0, len(candies)):
            if max_candies <= candies[i] + extraCandies:
                result.append(True)
            else:
                result.append(False)

        return result

