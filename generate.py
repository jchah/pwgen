import random
from string import ascii_uppercase, ascii_lowercase, digits
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-length", type=int, required=True)
args = parser.parse_args()

symbols = "!@#$%^&*()"
chars, pw = symbols + ascii_lowercase + ascii_uppercase + digits, ""


def check(*char):
    for p in char:
        if not any(c in p for c in pw):
            return 1


while check(symbols, ascii_lowercase, ascii_uppercase, digits):
    pw = ''.join(random.choices(chars, k=args.length))

print(f"password: {pw}")
