from typing import Protocol


class Double(Protocol):
    def __call__(self, arg: int) -> int:
        ...


def implementation1(arg: int) -> int:
    return 2 * arg


def implementation2(arg: int) -> int:
    return arg + arg


def faulty_implementation(arg: int) -> int:
    return 8

