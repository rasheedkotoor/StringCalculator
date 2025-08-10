class StringCalculator:
    """A simple string calculator"""

    def _is_number(self, string: str) -> bool:
        """Check if a string can be converted to a number."""
        try:
            float(string)
            return True
        except ValueError:
            return False

    def add(self, numbers: str) -> int:
        """
        Add numbers from a string input.
        Args:
            numbers (str): String containing numbers to add
        Returns:
            int: Sum of the numbers
        """
        if numbers == "":
            return 0
        numbers = numbers.replace("\n", ",")
        numbers = numbers.split(",")
        return sum(float(num) for num in numbers if self._is_number(num.strip()))
