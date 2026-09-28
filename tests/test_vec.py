import pytest
from src.vec import Vec3

@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        (Vec3(0., 0., 0.), Vec3(-2., -3., -4.), False),
        (Vec3(-2., -3., -4.), Vec3(-2., -3., -4.), True),
    ]
)
def test_eq(v1, v2, expected):
    assert (v1 == v2) == expected

@pytest.mark.parametrize(
    "v1, v2, expected_v",
    [
        # standard positive
        (Vec3(1., 2., 3.), Vec3(2., 3., 4.), Vec3(3., 5., 7.)),
        # zero + negative
        (Vec3(0., 0., 0.), Vec3(-2., -3., -4.), Vec3(-2., -3., -4.)),
        # floating point
        (Vec3(1.5, 2.5, 3.5), Vec3(0.5, 0.5, 0.5), Vec3(2., 3., 4.))
    ]
)
def test_vec_add(v1, v2, expected_v):
    result = v1 + v2

    assert result == expected_v
