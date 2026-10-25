import pytest

from calc import add, divide, average


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 0, 0),
        (0, 7, 7),
        (10**12, 1, 10**12 + 1),
    ],
)
def test_add_integers(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(0.5, 0.25, 0.75), (-1.5, 1.5, 0.0), (0.1, 0.2, 0.3), (1, 2.5, 3.5)],
)
def test_add_floats(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (7, 2, 3.5),
        (-6, 3, -2),
        (6, -3, -2),
        (-6, -3, 2),
        (0, 5, 0),
        (1, 3, 1 / 3),
        (5.5, 2.5, 2.2),
    ],
)
def test_divide_normal(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [1, 0, -1, 2.5])
def test_divide_by_zero_raises(a):
    with pytest.raises((ZeroDivisionError, ValueError)):
        divide(a, 0)


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 2),
        ([2, 4, 6, 8], 5),
        ([-1, -2, -3], -2),
        ([-5, 5], 0),
        ([0, 0, 0], 0),
        ([1.5, 2.5], 2.0),
        ([0.1, 0.2, 0.3], 0.2),
        ([10], 10),
        ([0], 0),
        ([-4.5], -4.5),
    ],
)
def test_average(numbers, expected):
    assert average(numbers) == pytest.approx(expected)


def test_average_empty_raises():
    with pytest.raises((ZeroDivisionError, ValueError)):
        average([])


def test_average_equals_sum_over_len():
    nums = [3, 9, 12, 7]
    assert average(nums) == pytest.approx(sum(nums) / len(nums))
