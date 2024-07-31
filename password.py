import random
import string

def generate_password(length=12, use_special_chars=True):
    """Generate a random password."""
    # Define the characters to use for the password
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Combine all characters
    all_characters = letters + digits + special_chars

    if not all_characters:
        raise ValueError("No characters available to generate the password")

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
        use_special_chars = input("Include special characters (y/n)? ").strip().lower() == 'y'
        
        if length < 1:
            print("Password length must be at least 1.")
            return
        
        password = generate_password(length, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
