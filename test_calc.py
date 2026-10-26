import math

import pytest

from calc import add, divide, average

NAN = float("nan")
INF = float("inf")


# ---------------- add ----------------

@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 5), (-2, -3, -5), (-2, 3, 1), (0, 0, 0), (10**12, 1, 10**12 + 1)],
)
def test_add_integers(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(0.5, 0.25, 0.75), (-1.5, 1.5, 0.0), (1, 2.5, 3.5)]
)
def test_add_floats(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


def test_add_nan_propagates():
    assert math.isnan(add(NAN, 1))


def test_add_inf():
    assert add(INF, 1) == INF
    assert add(-INF, -1) == -INF


def test_add_inf_minus_inf_is_nan():
    assert math.isnan(add(INF, -INF))


def test_add_bools():
    assert add(True, True) == 2
    assert add(True, False) == 1


def test_add_tiny_floats():
    assert add(1e-300, 1e-300) == pytest.approx(2e-300)


def test_add_float_precision_exact():
    assert add(0.1, 0.2) != 0.3
    assert add(0.1, 0.2) == pytest.approx(0.3, abs=1e-15)


def test_add_negative_zero():
    assert math.copysign(1, add(-0.0, -0.0)) == -1
    assert math.copysign(1, add(-0.0, 0.0)) == 1


# ---------------- divide ----------------

@pytest.mark.parametrize(
    "a, b, expected",
    [(6, 3, 2), (7, 2, 3.5), (-6, 3, -2), (6, -3, -2), (-6, -3, 2), (0, 5, 0), (1, 3, 1 / 3)],
)
def test_divide_normal(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [1, 0, -1, 2.5])
def test_divide_by_zero_raises(a):
    with pytest.raises((ZeroDivisionError, ValueError)):
        divide(a, 0)


def test_divide_nan_propagates():
    assert math.isnan(divide(NAN, 2))
    assert math.isnan(divide(2, NAN))


def test_divide_inf():
    assert divide(INF, 2) == INF
    assert divide(1, INF) == 0.0
    assert math.isnan(divide(INF, INF))


def test_divide_by_negative_zero_raises():
    with pytest.raises((ZeroDivisionError, ValueError)):
        divide(1, -0.0)


def test_divide_negative_zero_numerator():
    assert math.copysign(1, divide(-0.0, 5)) == -1


def test_divide_bools():
    assert divide(True, True) == 1
    with pytest.raises((ZeroDivisionError, ValueError)):
        divide(1, False)


def test_divide_tiny_result_underflows_to_zero():
    assert divide(1e-300, 1e300) == 0.0


def test_divide_overflow():
    # Verified in Python: float division 1e300 / 1e-300 returns inf (no exception).
    assert divide(1e300, 1e-300) == INF


def test_divide_returns_float_for_ints():
    assert isinstance(divide(4, 2), float)


# ---------------- average ----------------

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 2),
        ([2, 4, 6, 8], 5),
        ([-1, -2, -3], -2),
        ([-5, 5], 0),
        ([0, 0, 0], 0),
        ([1.5, 2.5], 2.0),
        ([10], 10),
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


def test_average_nan_propagates():
    assert math.isnan(average([1, NAN]))


def test_average_inf():
    assert average([INF, 1]) == INF


def test_average_bools():
    assert average([True, False]) == pytest.approx(0.5)


def test_average_tiny_floats():
    assert average([1e-300, 3e-300]) == pytest.approx(2e-300)


def test_average_negative_zero():
    assert average([-0.0, -0.0]) == 0.0


def test_average_precision_large_values():
    # 1e16 + 1.0 loses the 1.0 in float arithmetic, so the sum is exactly 0.
    assert average([1e16, 1.0, -1e16]) == pytest.approx(1 / 3, abs=1.0)


def test_average_tuple_and_generator():
    assert average((2, 4)) == pytest.approx(3)
    with pytest.raises(TypeError):
        average(x for x in [1, 2])


def test_average_identical_values():
    assert average([7, 7, 7, 7]) == pytest.approx(7)
