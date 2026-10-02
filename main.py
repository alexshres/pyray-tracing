import raytracer
from raytracer.vec import Vec3
from raytracer.ray import Ray

def main():
    v = Vec3(1., 2., 3.)

    origin = Vec3(1., 2., 4.)
    direction = Vec3(1., 1., 1.)

    print(f"{v=}")

    print(f"{v.length()=}")

    ray = Ray(origin, direction)

    print(f"{ray.at(1.)}")
    print(f"{ray.at(1.).length()}")



if __name__ == "__main__":
    main()
