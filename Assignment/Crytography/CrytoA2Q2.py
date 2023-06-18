# MDES S-box
s_box = [
    [0b10, 0b00, 0b11, 0b01],
    [0b00, 0b01, 0b10, 0b11],
]
def mdes_sbox(input_bits):
    # Convert the input bits to decimal
    row = input_bits[0] * 2 + input_bits[2]
    col = input_bits[1]

    # Look up the output in the S-box and convert it to binary
    output_dec = s_box[row][col]
    output_bits = [(output_dec >> i) & 1 for i in range(1, -1, -1)]

    return output_bits

def mdes_encrypt(plaintext, key):
    # Remove 0b from binary and convert to int list
    plaintext = [int(i) for i in str(bin(plaintext))[2:]]
    for i in range(4):
        if len(plaintext) < 4:
            plaintext.insert(0,0)
    # Remove 0b from binary and convert to int
    key = [int(i) for i in str(bin(key))[2:]]
    for i in range(2):
        if len(key) < 2:
            key.insert(0,0)
            
    # Produce keys K1 and K2 from key
    K1 = key[0] << 2 | key[0] << 1 | key[0]
    K2 = key[1] << 1 | key[1] << 1 | key[1]

    # Rotate plaintext left 1 bit
    plaintext = plaintext[1:] + [plaintext[0]]

    # Divide the input plaintext into two equal halves
    A0 = plaintext[:2]  # left half
    B0 = plaintext[2:]  # right half

    # Convert A0 and B0 to decimal
    A0 = A0[0] * 2 + A0[1]
    B0 = B0[0] * 2 + B0[1]

    #Round 1
    B1 = A0 ^ int(''.join(map(str, mdes_sbox([B0 & 0b10 >> 1, B0 & 0b01, K1]))), 2)
    A1 = B0

    #Round 2
    B2 = A1 ^ int(''.join(map(str, mdes_sbox([B1 & 0b10 >> 1, B1 & 0b01, K2]))), 2)
    A2 = B1

    # Swap A2 and B2 
    A2, B2 = B2, A2

    # Convert A2 and B2 to 2-bit binary strings
    A2 = bin(A2)[2:].zfill(2)
    B2 = bin(B2)[2:].zfill(2)

    # Concatenate B2 and A2 into a 4-bit ciphertext
    C = int(B2 + A2, 2)

    # Rotate C right 1 bit
    C = (C >> 1) | ((C & 0b1) << 3)

    return C
print("CSCI361 Assignment 2 LDES Block Cipher")
# Print all possible plaintext and ciphertext pairs for key 00
print("")
print("Key: 00")
for i in range(16):
    print("Plaintext: ", f"{i:04b}", " Ciphertext: ", f"{(mdes_encrypt(i, 0b00)):04b}")

# Print all possible plaintext and ciphertext pairs for key 01
print("")
print("Key: 01")
for i in range(16):
    print("Plaintext: ", f"{i:04b}", " Ciphertext: ", f"{(mdes_encrypt(i, 0b01)):04b}")

# Print all possible plaintext and ciphertext pairs for key 10
print("")
print("Key: 10")
for i in range(16):
    print("Plaintext: ", f"{i:04b}", " Ciphertext: ", f"{(mdes_encrypt(i, 0b10)):04b}")
    