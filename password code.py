import random
import string

def generate_password():
    try:
        # Get the desired password length from the user
        length = int(input("Enter the desired password length (minimum 4): "))
        
        if length < 4:
            print("Password length should be at least 4 for better security.")
            return

        # Define character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        # Ensure the password has at least one of each type of character
        all_characters = lower + upper + digits + special
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special),
        ]

        # Fill the rest of the password length with random choices
        password += random.choices(all_characters, k=length - 4)

        # Shuffle the password to randomize it further
        random.shuffle(password)

        # Convert the list to a string and display the password
        generated_password = ''.join(password)
        print(f"Generated Password: {generated_password}")

    except ValueError:
        print("Please enter a valid number.")

# Run the password generator
generate_password()
