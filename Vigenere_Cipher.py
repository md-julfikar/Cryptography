def gen_key(text: str, key:str)->str:
    text= text.upper()
    key= key.upper()

    repeated_key=""
    key_index=0

    for char in text:

        if char.isalpha():
            repeated_key+= key[key_index % len(key)]
            key_index+=1
        else:
            repeated_key += char
    return repeated_key

def encrypt(text:str, key:str)-> str:
    text=text.upper()
    key= gen_key(text,key)

    encrypted=""
    for t,k in  zip(text,key):
        if t.isalpha():
            encrypted+=chr((ord(t)-65 + ord(k)-65)%26 + 65)
        else:
            encrypted+=t
    return encrypted

def decrypt(text:str, key:str)-> str:
    text=text.upper()
    key=gen_key(text,key)

    decrypted= ""

    for t, k in zip(text, key):
        if t.isalpha():
            decrypted+=chr( ((ord(t)-65) - (ord(k)-65))%26 + 65)
        else:
            decrypted+=t
    return decrypted

text="Hello This is Rab"
key="Key"

e=encrypt(text, key)
t=decrypt(e,key)

print(f"Original Text: {text}")
print(f"Encrypted Message: {e}")
print(f"Decrypted Message: {t}")