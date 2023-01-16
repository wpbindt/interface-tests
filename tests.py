from main import Double


def test_double(double: Double) -> None:
    assert double(3) == 6


def test_double_with_4(double: Double) -> None:
    assert double(4) == 8
