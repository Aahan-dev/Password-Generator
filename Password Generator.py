import random
import string

class RandomPasswordGenerator:
    def __init__(self):
        """Initialize the password generator with character sets."""
        self.lowercase = string.ascii_lowercase  # a-z
        self.uppercase = string.ascii_uppercase  # A-Z
        self.digits = string.digits              # 0-9
        self.symbols = string.punctuation         # Special characters
        self.all_characters = self.lowercase + self.uppercase + self.digits + self.symbols

    def generate_password(self, length):
        """
        Generate a random password of specified length.

        Args:
            length (int): The desired length of the password.

        Returns:
            str: A randomly generated password.
        """
        if length < 4:
            raise ValueError("Password length should be at least 4 characters.")

        # Ensure password contains at least one of each character type
        password = [
            random.choice(self.lowercase),
            random.choice(self.uppercase),
            random.choice(self.digits),
            random.choice(self.symbols)
        ]

        