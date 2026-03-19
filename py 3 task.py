import random
import string

print("---- PASSWORD GENERATOR ----")

# Take input
length = int(input("Enter password length: "))

# Define characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Display password
print("Generated Password:", password)