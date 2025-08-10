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
        assert result == 5

    def test_two_numbers_returns_sum(self):
        """Test that two numbers return their sum."""
        result = self.calculator.add("1,2")
        assert result == 3

    def test_many_numbers_returns_sum(self):
        """Test that many numbers return their sum."""
        result = self.calculator.add("1,2,3,4,5")
        assert result == 15

    def test_numbers_with_spaces_returns_sum(self):
        """Test that numbers with spaces return the correct sum."""
        result = self.calculator.add(" 1 , 2 , 3 ")
        assert result == 6
