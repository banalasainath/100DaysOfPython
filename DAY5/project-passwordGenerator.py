import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

letters_count = int(input("How many letters should be present in your password?\n"))
numbers_count = int(input("How many numbers should be present in your password?\n"))
symbols_count = int(input("How many symbols should be present in your password?\n"))

password = []
for letter in range(letters_count):
    password.append(random.choice(letters))

for number in range(numbers_count):
    password.append(random.choice(numbers))

for symbol in range(symbols_count):
    password.append(random.choice(symbols))

random.shuffle(password)
password = ''.join(password)
print(f"Your Password: {password}")
