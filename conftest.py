from typing import Iterator

import pytest

from main import implementation1, implementation2, faulty_implementation, Double


@pytest.fixture
def double1() -> Iterator[Double]:
    yield implementation1


@pytest.fixture
def double2() -> Iterator[Double]:
    yield implementation2


@pytest.fixture
def double3() -> Iterator[Double]:
    yield faulty_implementation


@pytest.fixture(
    params=[
        double1.__name__,
        double2.__name__,
        double3.__name__,
    ]
)
def double(request) -> Double:
    return request.getfixturevalue(request.param)

