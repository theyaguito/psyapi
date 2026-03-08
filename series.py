from __future__ import annotations
from typing import List
import numpy as np


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

    # Matrix multiplication algorithm for Fibonacci numbers
    def get(self) -> int:
        if self.n == 0:
            return 0
        # T Matrix
        T: np.ndarrray = np.array([[1, 1], [1, 0]], dtype=object)  # Allow big ints
        result: int = np.linalg.matrix_power(T, self.n - 1)
        return result[0][0]


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
