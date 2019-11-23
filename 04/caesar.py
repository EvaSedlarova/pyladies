ciphertext = ''
key = -1
plaintext = input("Zadej zprávu na šifrování: ")


while key < 0:
    key_input = input("Zadej klíč k šifře: ")

    try:
        key = int(key_input)
        
    except ValueError:
        pass


for i in plaintext:

    if 64 < ord(i) < 91:
        ciphertext += chr((ord(i) + key - 65) % 26 + 65)
        
    elif 96 < ord(i) < 123:
        ciphertext += chr((ord(i) + key - 97) % 26 + 97)

    else:
        ciphertext += i

print(ciphertext)