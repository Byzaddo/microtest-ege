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


def skip(reason: str = "Skipped"):
    """
    Register a test but mark it as skipped.

    Usage:

        @skip("Not implemented yet")
        def test_something():
            ...
    """

    def decorator(test_func):
        _TESTS.append(
            TestCase(
                func=test_func,
                name=test_func.__name__,
                skip_reason=reason,
            )
        )
        return test_func

    return decorator

def get_tests() -> list[TestCase]:
    """
    Return a copy of all registered tests.
    """
    return list(_TESTS)

def clear_tests() -> None:
    """
    Clear the test registry.

    Mostly useful internally or for advanced usage.
    """
    _TESTS.clear()