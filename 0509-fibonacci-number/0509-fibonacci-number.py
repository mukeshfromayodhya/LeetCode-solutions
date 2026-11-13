class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return 0
        elif n== 1:
            return 1
        for i in range(2, n + 1):
            fib = a + b
            a = b
            b = fib
        return b
        