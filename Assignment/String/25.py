''' Write a Python program to create a Caesar encryption.

Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or 
Caesar shift,is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter 
some fixed number of positions down the alphabet. 
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
The method is named after Julius Caesar, who used it in his private correspondence.'''

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha(): 
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_encrypt(plaintext, shift)
print("Plaintext:", plaintext)
print("Shift:", shift)
print("Encrypted text:", encrypted_text)
