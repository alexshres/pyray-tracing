from __future__ import annotations

import math
from typing import Self


class Vec3:
    def __init__(self, e0: float, e1: float, e2: float):
        self.vec = [e0, e1, e2]

    @classmethod 
    def from_list(cls, vec_list: list):
        if len(vec_list) != 3:
            raise ValueError("List passed in must have exactly 3 elements")

        e0, e1, e2 = vec_list
        return cls(e0, e1, e2)

    def __getitem__(self, index:int):
        if index > 2:
            raise ValueError("Index must be between 0 and 2.")

        return self.vec[index]

    def __neg__(self) -> Vec3:
        # return Vec3(-1* self.vec[0], -1*self.vec[1], -1*self.vec[2])
        # return Vec3(*[-x for x in self.vec])
        return Vec3.from_list([-x for x in self.vec])

    def __iadd__(self, other: Self) -> Self:
        self.vec = [x1 + x2 for x1, x2 in zip(self.vec, other.vec)]

        return self

    def __imul__(self, scalar: float) -> Self:
        self.vec = [scalar * x for x in self.vec]

        return self

    def __itruediv__(self, scalar: float) -> Self:
        if scalar == 0.0:
            raise ZeroDivisionError

        self.vec = [x/scalar for x in self.vec]
        return self

    def length_squared(self) -> float:
        return sum([x**2 for x in self.vec])

    def length(self) -> float:
        return math.sqrt(self.length_squared())



