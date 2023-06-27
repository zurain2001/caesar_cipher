"""
# Program: Caesar Cipher
# Date: 26 June 2023
# Developer: Zurain Zeeshan

"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


import art

print(art.logo)


def caesar(plain_text, shift_amount, direct):
    word = ""
    for letter in plain_text:
        if direct == 'encode':
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                word += new_letter
            else:
                word += letter
        elif direct == 'decode':
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                word += new_letter
            else:
                word += letter
    print(f"The new text is {word}")

keep_going = True
while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, direct=direction)

    restart = input("Do you want to go again? ").lower()
    if restart == 'no':
        keep_going = False
        print("Goodbye.")
    else:
        keep_going = True

