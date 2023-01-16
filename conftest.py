import pytest

from main import implementation1, implementation2, faulty_implementation


@pytest.fixture
def double1():
    yield implementation1


@pytest.fixture
def double2():
    yield implementation2


@pytest.fixture
def double3():
    yield faulty_implementation


@pytest.fixture(
    params=[
        double1.__name__,
        double2.__name__,
        double3.__name__,
    ]
)
def double(request):
    return request.getfixturevalue(request.param)

