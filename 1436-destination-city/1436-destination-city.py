class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()

        for path in paths:
            sources.add(path[0])

        for path in paths:
            if path[1] not in sources:
                return path[1]