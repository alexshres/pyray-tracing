from __future__ import annotations

import math
from typing import Self


class Vec3:
    def __init__(self, e0: float, e1: float, e2: float):
        self.vec = [e0, e1, e2]

    @classmethod 
    def from_list(cls, vec_list: list) -> Self:
        if len(vec_list) != 3:
            raise ValueError("List passed in must have exactly 3 elements")

        e0, e1, e2 = vec_list
        return cls(e0, e1, e2)

    @classmethod
    def origin(cls) -> Self:
        return cls(0.0, 0.0, 0.0)

    def __getitem__(self, index:int):
        if index > 2:
            raise ValueError("Index must be between 0 and 2.")

        return self.vec[index]

    def __neg__(self) -> Vec3:
        # return Vec3(-1* self.vec[0], -1*self.vec[1], -1*self.vec[2])
        # return Vec3(*[-x for x in self.vec])
        return Vec3.from_list([-x for x in self.vec])

    def __add__(self, other: Vec3) -> Vec3:
        return Vec3.from_list([x+y for x, y in zip(self.vec, other.vec)])

    def __sub__(self, other: Vec3) -> Vec3:
        return Vec3.from_list([x-y for x, y in zip(self.vec, other.vec)])

    def __iadd__(self, other: Self) -> Self:
        self.vec = [x1 + x2 for x1, x2 in zip(self.vec, other.vec)]

        return self

    def __mul__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3.from_list([x*y for x, y in zip(self.vec, other.vec)])
        elif isinstance(other, (int, float)):
            return Vec3.from_list([other*x for x in self.vec])
        else:
            return NotImplemented

    def __rmul__(self, scalar: int | float) -> Vec3:
        return self.__mul__(scalar)

    def __imul__(self, scalar: float) -> Self:
        self.vec = [scalar * x for x in self.vec]

        return self

    def __truediv__(self, scalar: int | float):
        if scalar == 0:
            raise ZeroDivisionError

        return Vec3.from_list([x/scalar for x in self.vec])

    def __itruediv__(self, scalar: int | float) -> Self:
        if scalar == 0.0:
            raise ZeroDivisionError

        self.vec = [x/scalar for x in self.vec]
        return self

    def __eq__(self, other: Self) -> bool:
        return all([math.isclose(x, y) for x, y in zip(self.vec, other.vec)])

    def __repr__(self):
        return f"Vec3({self.vec}"

    def length_squared(self) -> float:
        return sum([x**2 for x in self.vec])

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def dot(self, other: Self) -> float:
        return sum([x*y for x,y in zip(self.vec, other.vec)])

    def cross(self, other: Self) -> Vec3:
        return Vec3(
                    self.vec[1]*other.vec[2] - self.vec[2]*other.vec[1],
                    self.vec[2]*other.vec[0] - self.vec[0]*other.vec[2],
                    self.vec[0]*other.vec[1] - self.vec[1]*other.vec[0]
                )

    def unit_vector(self) -> Vec3:
        return self/self.length()

        



