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

    def test_numbers_with_strings(self):
        """Test numbers with strings return the correct sum, ignoring non-numerics."""
        result = self.calculator.add("1,2,3,a,4,b")
        assert result == 10

    def test_new_line_delimiter(self):
        """Test that new line as a delimiter works correctly."""
        result = self.calculator.add("1\n2,3")
        assert result == 6

    def test_floating_point_numbers(self):
        """Test that floating point numbers are handled correctly."""
        result = self.calculator.add("1,2.5,3")
        assert result == 6.5

    def test_negative_numbers(self):
        """Test that negative numbers are handled correctly."""
        result = self.calculator.add("1,-2,3,-10")
        assert result == -8
