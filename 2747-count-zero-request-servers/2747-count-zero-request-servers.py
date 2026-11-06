class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        result = [0] * len(queries)

        active = {}
        left = 0
        right = 0
        active_count = 0

        for q, idx in sorted_queries:

            start = q - x

            # Add logs whose timestamp is <= query time
            while right < len(logs) and logs[right][1] <= q:
                server_id = logs[right][0]

                if active.get(server_id, 0) == 0:
                    active_count += 1

                active[server_id] = active.get(server_id, 0) + 1

                right += 1

            # Remove logs outside the time window
            while left < right and logs[left][1] < start:
                server_id = logs[left][0]

                active[server_id] -= 1

                if active[server_id] == 0:
                    active_count -= 1
                    del active[server_id]

                left += 1

            result[idx] = n - active_count

        return result
