# interface-tests

Illustrates how to automatically run the same test for different implementations of an interface using `pytest`.

The example tests an interface `Double` (which is basically `Callable[[int], int]`), which has three 
implementations, `implementation1/2` and `faulty_implementation`, all contained in `main.py`. There are two 
tests, contained in `tests.py`, which are run for each implementation of `Double`. Run the tests using
```
make run-tests
```
