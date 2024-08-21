import random
import string

def generate_password(length=12):
    # Ensure the password has at least one of each character type
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the remaining length with random characters
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the characters to avoid a predictable pattern
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
password = generate_password(16)  # Generates a 16-character password
print("Generated Password:",password)
