class StringCalculator:
    """A simple string calculator"""

    def _is_number(self, string) -> bool:
        """Check if a string can be converted to a number."""
        try:
            float(string)
            return True
        except ValueError:
            return False

    def add(self, numbers_string) -> int:
        """
        Add numbers from a string input.
        Args:
            numbers_string (str): String containing numbers to add
        Returns:
            int: Sum of the numbers
        """
        if numbers_string == "":
            return 0
        numbers_string = numbers_string.replace("\n", ",")
        numbers = numbers_string.split(",")
        return sum(float(x) for x in numbers if self._is_number(x.strip()))
