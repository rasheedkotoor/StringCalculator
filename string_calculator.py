class StringCalculator:
    """A simple string calculator"""
    
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
        if "," not in numbers_string:
            return int(numbers_string)
