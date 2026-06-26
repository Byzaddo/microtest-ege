from dataclasses import dataclass
from typing import Callable


@dataclass
class TestCase:
    func: Callable
    name: str
    skip_reason: str | None = None


_TESTS: list[TestCase] = []


def test(func=None, *, name: str | None = None):
    """
    Register a function as a test.

    Usage:

        @test
        def test_addition():
            ...

    Or:

        @test(name="custom name")
        def some_test():
            ...
    """

    def decorator(test_func):
        test_name = name or test_func.__name__
        _TESTS.append(TestCase(func=test_func, name=test_name))
        return test_func

    if func is None:
        return decorator

    return decorator(func)

