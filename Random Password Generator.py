import random
import string

def generate_password(password_length, include_letters=True, include_numbers=True, include_symbols=True):
    # Define character sets based on user preferences
    character_set = ""
    if include_letters:
        character_set += string.ascii_letters
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation

    # Check if at least one character set is selected
    if not character_set:
        print("Error: Please select at least one character set.")
        return None

    # Generate the password
    generated_password = ''.join(random.choice(character_set) for _ in range(password_length))
    return generated_password

def main():
    print("--------------Password Generator--------------")

    # Get user preferences
    password_length = int(input("Enter the length of the password: "))
    include_letters = input("Include letters? (n/y): ").lower() == 'y'
    include_numbers = input("Include numbers? (n/y): ").lower() == 'y'
    include_symbols = input("Include symbols? (n/y): ").lower() == 'y'

    # Generate the password
    generated_password = generate_password(password_length, include_letters, include_numbers, include_symbols)

    # Display the generated password
    if generated_password:
        print(f"Your generated password is: {generated_password}")

if __name__ == "__main__":
    main()
