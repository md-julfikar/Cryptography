def rail_fence_encrypt(text, rails):
    if rails == 1:
        return text

    fence = ['' for _ in range(rails)]
    row = 0
    direction = 1

    for char in text:
        fence[row] += char

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


def rail_fence_decrypt(cipher, rails):
    if rails == 1:
        return cipher

    pattern = [['' for _ in range(len(cipher))] for _ in range(rails)]

    row = 0
    direction = 1

    for col in range(len(cipher)):
        pattern[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if pattern[i][j] == '*' and index < len(cipher):
                pattern[i][j] = cipher[index]
                index += 1

    result = ''
    row = 0
    direction = 1

    for col in range(len(cipher)):
        result += pattern[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return result



text = "HELLO WORLD"
rails = 3

encrypted = rail_fence_encrypt(text, rails)
decrypted = rail_fence_decrypt(encrypted, rails)

print("Original :", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)