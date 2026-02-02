
import random
import string

# step 1 generate a random password
def generate_password(length=8):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_letters) + ''.join(random.choice(characters) for _ in range(length - 1))
    return password

length = int(input("Enter the desired password length (minimum 8): "))
password = generate_password(length)

print(f"Generated Password: {password}")


# -----------------------------------------------------------------------------------------------------------`


# Random Password Generator
import random, string

# Step 1: Define Password Generation Function

def generate_password(length=12):
  if length < 4:
    raise ValueError("Password length must be at least 4 characters")

  # Character sets for the password
  uppercase = string.ascii_uppercase
  lowercase = string.ascii_lowercase
  digits = string.digits
  special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

  # Ensure at least one of each character type
  password = [
      random.choice(uppercase),
      random.choice(lowercase),
      random.choice(digits),
      random.choice(special_chars)
  ]

  # Fill the remaining length with random choices from all sets
  all_chars = uppercase + lowercase + digits + special_chars
  password += random.choices(all_chars, k=length - 4)

  # Shuffle the password to make it more random
  random.shuffle(password)

  # Convert the list to a string and return
  return ''.join(password)

# STep 2: User Interaction

try:
  length = int(input("Enter the desired password length (minimum 4): "))
  password = generate_password(length)
  print("Generated Password:", password)
except ValueError as e:
  print(e)