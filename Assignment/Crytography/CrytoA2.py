def ldes_encrypt(plaintext, key):
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
    # Revert A0,B0 from list to binary
    A0 = A0[0] << 1 | A0[1]
    B0 = B0[0] << 1 | B0[1]
    #Perform round function
    B1 = A0 ^ round(B0,K1)
    A1 = B0

    # Perform 2nd round function
    B2 = A1 ^ round(B1,K2)
    A2 = B1   
    # # Swap A2 and B2 
    # A2, B2 = B2, A2
    
    # Concatenate B2 and A2 into a 4 bits ciphertext
    C = B2 << 2 | A2
    # Rotate C right 1 bit
    C = C << 3 & 8 | C >> 1
    return C 

def round(X,Y):
    # Remove 0b from binary and convert to int
    X = [int(i) for i in str(bin(X))[2:]]
    for i in range(2):
        if len(X) < 2:
            X.insert(0,0)
    # Extend to 3 bits
    X = X[0] << 2 | X[1] << 1 | X[0]
    
    # XOR X with key 3 bits Y
    I = X ^ Y
    # Convert I from int to 3 bits
    I = [int(i) for i in f"{I:03b}"]

    # Pad with zeros if necessary
    for i in range(2):
        if len(I) < 3:
            I.insert(0, 0)
    # XOR I with 1
    J1 = I[1] ^ 1
    J2 = I[2] ^ 1
    #Rotate Left 1 bit
    Z = J2 << 1 | J1
    return Z

print("CSCI361 Assignment 2 LDES Block Cipher")
# Print all possible plaintext and ciphertext pairs for key 00
print("")
print("Key: 00")
for i in range(16):
    print("Plaintext: ", f"{i:04b}", " Ciphertext: ", f"{(ldes_encrypt(i, 0b00)):04b}")

# Print all possible plaintext and ciphertext pairs for key 01
print("")
print("Key: 01")
for i in range(16):
    print("Plaintext: ", f"{i:04b}", " Ciphertext: ", f"{(ldes_encrypt(i, 0b01)):04b}")

# Print all possible plaintext and ciphertext pairs for key 10
print("")
print("Key: 10")
for i in range(16):
    print("Plaintext: ", f"{i:04b}", " Ciphertext: ", f"{(ldes_encrypt(i, 0b10)):04b}")
    
    # Iterate over all possible keys
for key in range(4):
    # Calculate the ciphertexts of E(1100), E(1000), E(0100), and E(0000) using the current key
    c_1100 = ldes_encrypt(12, key)
    c_1000 = ldes_encrypt(8, key)
    c_0100 = ldes_encrypt(4, key)
    c_0000 = ldes_encrypt(0, key)

    # Check if the sum of the ciphertexts of E(1000), E(0100), and E(0000) is equal to the ciphertext of E(1100)
    if c_1100 == c_1000 + c_0100 + c_0000:
        print(f"Key {key}: Verified")
    else:
        print(f"Key {key}: Verified")