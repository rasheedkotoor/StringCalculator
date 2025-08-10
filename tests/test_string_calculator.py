import sys
import os

from StringCalculator.string_calculator import StringCalculator


class TestStringCalculator:

    def setup_method(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        """Test that empty string returns 0."""
        result = self.calculator.add("")
        assert result == 0

    def test_single_number_returns_itself(self):
        """Test that a single number returns itself."""
        result = self.calculator.add("5")
        # RED: This test will fail.
        assert result == 5
