from .vec import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3):
        self._origin = origin
        self._direction = direction

    @property
    def origin(self) -> Vec3:
        return self._origin

    @property
    def direction(self) -> Vec3:
        return self._direction

    def at(self, t: float) -> Vec3:
        return self._origin + t*self._direction
