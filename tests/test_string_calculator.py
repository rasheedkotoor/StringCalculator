import sys
import os

from StringCalculator.string_calculator import StringCalculator


class TestStringCalculator:

    def setup_method(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        """Test that empty string returns 0."""
        # RED - this test will fail.
        result = self.calculator.add("")
        assert result == 0
