import numpy as np

def inverse_mod (num:int, mod:int)->int:
    return pow(num, -1, mod)

def matrix_mod_inverse(matrix, mod):
    det=np.round(np.linalg.det(matrix))
    det= int(det % mod)

    det_inv= inverse_mod(det,mod)

    adj= np.round(det * np.linalg.inv(matrix)).astype(int)

    return (det_inv * adj) % mod

def hill_cipher_encrypt(text:str, key:np.ndarray)->str:
    text=text.upper().replace(" ",'')
    n=key.shape[0]
    r= len(text) % n
    if r !=0 :
        text+= 'X' * (n-r)

    result= ""

    for i in range(0, len(text), n):
        block= np.array([[ord(c)- 65] for c in text[i:i+n]])
        encrypted= np.dot(key, block) % 26
        for j in range(n):
            result+= chr(encrypted[j][0]+65)
    
    return result

def hill_cipher_decrypt(text:str, key:np.ndarray)->str:
    key_inv=matrix_mod_inverse(key,26)
    result=""

    n= key.shape[0]

    for i in range(0, len(text), n):
        block= np.array([[ord(c)-65] for c in text[i:i+n]])
        decrypted= np.dot(key_inv, block) % 26

        for j in range(n):
            result+=chr(decrypted[j][0]+65)
    return result


text="ThankYOU"

key=np.array([[3,3],[2,5]])
encrypted=hill_cipher_encrypt(text, key)

decrypted= hill_cipher_decrypt(encrypted, key)


print(encrypted, decrypted)
        
        
