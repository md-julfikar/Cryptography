def encode(text:str, key:int):
    encrypted=""
    for char in text:
        if char.isalpha():
            shift_base= 65 if char.isupper() else 97
            encrypted_char=chr((ord(char)-shift_base+key)%26 + shift_base)
            encrypted+=encrypted_char
        else:
            encrypted+=char
    return encrypted

def decode(text:str, key:int):
    decrypted=""
    for char in text:
        if char.isalpha():
            shift_base= 65 if char.isupper() else 97
            decrypted_char= chr((ord(char)-shift_base - key)%26 + shift_base)
            decrypted+=decrypted_char
        else:
            decrypted+=char
    return decrypted
st="AMDthisIS%"

e=encode(st,10)
d=decode(e,10)

print(f"{e}, {d}")