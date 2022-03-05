def encrypt(text, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_text = ""
    for character in text:
        index = (alphabet.index(character) + shift) % len(alphabet)
        new_text += alphabet[index]
    print(f"Your encrypted text is {new_text}.")

def decrypt(text, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_text = ""
    for character in text:
        index = (alphabet.index(character) - shift) % len(alphabet)
        new_text += alphabet[index]
    print(f"your decrypted text is {new_text}.")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else: 
    print(f"You typed an incorrect mode: {direction}.")
