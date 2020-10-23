#linear search version
import sys

if len(sys.argv) == 1:
    print("Usage: linear_substitution.py <key>")
    sys.exit()
elif len(sys.argv) > 2:
    print("The program only takes one key, please try again")
    sys.exit()
elif len(sys.argv[1]) < 26 or len(sys.argv[1]) > 26:
    print("The key must be 26 characters long, please try again")
    sys.exit()
else:
    key = sys.argv[1]

up_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_alph = "abcdefghijklmnopqrstuvwxyz"
message = input("Enter message\n$ ")

up_key = key.upper()
low_key = key.lower()

ciph_text = ""
for i in range(len(message)):
    j = 0
    flag = False

    if message[i].isalpha():
        if message[i].isupper():
            while not flag:
                if message[i] == up_alph[j]:
                    ciph_text += up_key[j]
                    flag = True
                else:
                    j += 1
        else:
            while not flag:
                if message[i] == low_alph[j]:
                    ciph_text += low_key[j]
                    flag = True
                else:
                    j += 1
    else:
        ciph_text += message[i]

print(ciph_text)