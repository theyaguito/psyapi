from __future__ import annotations
from typing import List


class Series:
    def __init__(self, n: int) -> None:
        self.n = n


class FibonacciSeries(Series):
    def gen(self) -> List[int]:
        result: List[int] = []
        a, b = 0, 1
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        return result


class ArithmeticSeries(Series):
    def __init__(self, n: int, start: int, diff: int) -> None:
        super().__init__(n)
        self.start = start
        self.diff = diff

    def gen(self) -> List[int]:
        result: List[int] = []
        curr = self.start
        for _ in range(self.n):
            result.append(curr)
            curr += self.diff
        return result
