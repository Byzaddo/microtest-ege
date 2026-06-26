class Expect:
    def __init__(self, value):
        self.value = value

    def to_equal(self, expected):
        if self.value != expected:
            raise AssertionError(
                f"Expected {self.value!r} to equal {expected!r}"
            )
        return self

    def to_not_equal(self, expected):
        if self.value == expected:
            raise AssertionError(
                f"Expected {self.value!r} to not equal {expected!r}"
            )
        return self
    
    def to_be_true(self):
        if self.value is not True:
            raise AssertionError(f"Expected {self.value!r} to be True")
        return self

    def to_be_false(self):
        if self.value is not False:
            raise AssertionError(f"Expected {self.value!r} to be False")
        return self

    def to_be_truthy(self):
        if not self.value:
            raise AssertionError(f"Expected {self.value!r} to be truthy")
        return self

    def to_be_falsy(self):
        if self.value:
            raise AssertionError(f"Expected {self.value!r} to be falsy")
        return self

    def to_be_none(self):
        if self.value is not None:
            raise AssertionError(f"Expected {self.value!r} to be None")
        return self

    def to_not_be_none(self):
        if self.value is None:
            raise AssertionError("Expected value to not be None")
        return self

    def to_be_greater_than(self, expected):
        if not self.value > expected:
            raise AssertionError(
                f"Expected {self.value!r} to be greater than {expected!r}"
            )
        return self

    def to_be_less_than(self, expected):
        if not self.value < expected:
            raise AssertionError(
                f"Expected {self.value!r} to be less than {expected!r}"
            )
        return self

    def to_be_between(self, lower, upper, *, inclusive=True):
        if inclusive:
            passed = lower <= self.value <= upper
            condition = f"between {lower!r} and {upper!r}, inclusive"
        else:
            passed = lower < self.value < upper
            condition = f"between {lower!r} and {upper!r}, exclusive"

        if not passed:
            raise AssertionError(
                f"Expected {self.value!r} to be {condition}"
            )

        return self

    def to_be_close_to(self, expected, tolerance=1e-6):
        difference = abs(self.value - expected)

        if difference > tolerance:
            raise AssertionError(
                f"Expected {self.value!r} to be close to {expected!r}. "
                f"Difference was {difference!r}, tolerance was {tolerance!r}."
            )

        return self

    def to_contain(self, item):
        if item not in self.value:
            raise AssertionError(
                f"Expected {self.value!r} to contain {item!r}"
            )
        return self

    def to_not_contain(self, item):
        if item in self.value:
            raise AssertionError(
                f"Expected {self.value!r} to not contain {item!r}"
            )
        return self

    def to_have_length(self, expected_length):
        actual_length = len(self.value)

        if actual_length != expected_length:
            raise AssertionError(
                f"Expected length {expected_length!r}, "
                f"but got {actual_length!r}"
            )

        return self

    def to_be_instance_of(self, expected_type):
        if not isinstance(self.value, expected_type):
            raise AssertionError(
                f"Expected {self.value!r} to be an instance of "
                f"{expected_type.__name__}, but got {type(self.value).__name__}"
            )

        return self

    def to_raise(self, expected_error, *, message_contains: str | None = None):
        """
        Check that a callable raises a specific error.

        Example:

            expect(lambda: int("abc")).to_raise(ValueError)
        """

        if not callable(self.value):
            raise AssertionError(
                "to_raise() expects a callable. "
                "Example: expect(lambda: int('abc')).to_raise(ValueError)"
            )

        try:
            self.value()

        except expected_error as error:
            if message_contains is not None:
                error_message = str(error)

                if message_contains not in error_message:
                    raise AssertionError(
                        f"Expected error message to contain "
                        f"{message_contains!r}, but got {error_message!r}"
                    )

            return self

        except Exception as error:
            raise AssertionError(
                f"Expected {expected_error.__name__}, "
                f"but got {type(error).__name__}: {error}"
            )

        raise AssertionError(
            f"Expected {expected_error.__name__}, but no error was raised"
        )


def expect(value):
    return Expect(value)