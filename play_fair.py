def gen_key_matrix(key:str)->list:
    key=key.upper().replace('I',"J")
    matrix=[]
    used=set()
    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)
    for char in "abcdefghjklmnopqrstuvwxyz".upper():
        if char not in used:
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0,25,5)]


key="Test"
key_matrix=gen_key_matrix(key)

print(key_matrix)

def find_index(matrix:list):
    t=dict()
    for row in range(5):
        for col in range(5):
            t[matrix[row][col]]= (row,col)
    return t;



def prepare_text(text:str):

    text=text.upper().replace('I','J')

    text=''.join(filter(str.isalpha,text))

    prepared=""
    i=0;
    while i < len(text):
        a=text[i]
        b=text[i+1] if i+1< len(text) else "X"
    
        if a==b:
            prepared+= a + 'X'
            i += 1
        else:
            prepared+= a+ b
            i += 2
    
    if len(prepared) %2 !=0:
        prepared += 'X'

    return prepared

def playFair_encrypt(text:str, key_matrix:list)->str:
    '''Main Encrypt Function'''
    text=prepare_text(text)
    encrypted=""
    index=find_index(key_matrix)

    for i in range(0,len(text),2):
        a,b=text[i], text[i+1]
        row1,col1=index[a]
        row2,col2=index[b]

        if row1==row2:
            encrypted += key_matrix[row1][(col1+1)%5]
            encrypted += key_matrix[row2][(col2+1)%5]
        elif col1==col2:
            encrypted += key_matrix[(row1+1)%5][col1]
            encrypted += key_matrix[(row2+1)%5][col2]
        else:
            encrypted+=key_matrix[row1][col2]
            encrypted+=key_matrix[row2][col1]
        
    return encrypted

def playFair_decrypt(text:str, key_matrix: list) -> str:
    '''Decrypt Function'''
    decrypted=""
    index=find_index(key_matrix)
    for i in range(0, len(text), 2):
        a,b = text[i], text[i+1]
        row1, col1= index[a]
        row2, col2= index[b]
        if row1==row2:
            decrypted+= key_matrix[row1][(col1-1)%5]
            decrypted+= key_matrix[row2][(col2-1)%5]
        elif col1==col2:
            decrypted+= key_matrix[(row1-1)%5][col1]
            decrypted+= key_matrix[(row2-1)%5][col2]
        else:
            decrypted+=key_matrix[row1][col2]
            decrypted+=key_matrix[row2][col1]
    return decrypted;

text="This is THe Test Str"
encrypted=playFair_encrypt(text,key_matrix);
decrypted= playFair_decrypt(encrypted, key_matrix)
print(encrypted, decrypted)
