import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    # Combine all selected characters
    all_characters = lowercase + uppercase + numbers + special

    # Ensure there's at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special:
        password.append(random.choice(special))
    password.append(random.choice(lowercase))

    # Fill the rest of the password
    for _ in range(length - len(password)):
        password.append(random.choice(all_characters))

    # Shuffle the password to randomize character order
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # Get user preferences
    length = int(input("Enter the desired password length (minimum 4): "))
    if length < 4:
        print("Password length must be at least 4. Setting to default length of 12.")
        length = 12

    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print("\nGenerated Password: ", password)

if __name__ == "__main__":
    main()
