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
        numbers = numbers_string.split(",")
        return sum(int(x) for x in numbers)
