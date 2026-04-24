import random

def gcd(num1:int, num2:int)->int:
    if num1==0: 
        return num2
    return gcd(num2%num1, num1)


def is_prime(num:int)->bool:
    if num<2: 
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
            return False
    return True

def gen_prime()->int:
    num=random.randint(10000000, 10001000)
    while not is_prime(num):
        num=random.randint(10000000, 10001000)
    return num

def mod_inverse(e:int, phi:int)->int:
    return pow(e,-1,phi)


def gen_key_pair():

    p=gen_prime()
    q=gen_prime()

    while p==q:
        q=gen_prime()
    n = p* q

    phi = (p-1) * (q-1)

    e=2
    while e< phi:
        if gcd(e,phi)==1:
            break
        e+=1
    
    d=mod_inverse(e,phi)

    return (e,n), (d,n)

def encrypt(text:str, public_key_pair:tuple)-> list:
    e,n=public_key_pair
    encrypted =[(pow(ord(char),e,n)) for char in text]
    return encrypted
def decrypt(text:list, private_key_pair:tuple)-> str:
    d,n= private_key_pair
    decrypted= ''.join(chr(pow(char, d, n)) for char in text)
    return decrypted

public_key, private_key=gen_key_pair()

text="Hello"

encrypted=encrypt(text, public_key)
decrypted=decrypt(encrypted, private_key)
print(encrypted, decrypted)


