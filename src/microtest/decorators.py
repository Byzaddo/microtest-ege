from dataclasses import dataclass # to store test case inforation
from typing import Callable # to type hnt the function type 


@dataclass
class TestCase: # to store information about THE test case
    func: Callable
    name: str
    skip_reason: str | None = None


_TESTS: list[TestCase] = []


def test(func=None, *, name: str | None = None): # to register the func as a test, can name if want


    def decorator(test_func):
        test_name = name or test_func.__name__
        _TESTS.append(TestCase(func=test_func, name=test_name))
        return test_func

    if func is None:
        return decorator

    return decorator(func)


def skip(reason: str = "Skipped"):    # to register a test but skip it 

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