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

        # Fill the rest of the password length with random characters
        password += random.choices(self.all_characters, k=length - 4)


        # Shuffle the created password to ensure randomness
        random.shuffle(password)


        return ''.join(password)


    def run(self):
        """Run the password generator tool."""
        while True:
            try:
                length = int(input("Enter desired password length (min 4): "))
                password = self.generate_password(length)
                print(f"Generated Password: {password}")
            except ValueError as e:
                print(e)


            # Check if the user wants to generate another password
            repeat = input("Do you want to generate another password? (yes/no): ").strip().lower()
            if repeat != 'yes':
                print("Exiting the password generator. Goodbye!")
                break


if __name__ == "__main__":
    # Create an instance of RandomPasswordGenerator and run it
    password_generator = RandomPasswordGenerator()
    password_generator.run()