import random
import sys
from string import ascii_uppercase, ascii_lowercase, digits

symbols = "!@#$%^&*()"
chars, pw = symbols + ascii_lowercase + ascii_uppercase + digits, ""


def check(*char):
    for p in char:
        if not any(c in p for c in pw):
            return 1


while check(symbols, ascii_lowercase, ascii_uppercase, digits):
    pw = ''.join(random.choices(chars, k=int(sys.argv[1])))

print(f"password: {pw}")
