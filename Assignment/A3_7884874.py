import random
from typing import Tuple

# Generate 5-digit prime numbers p and q
def generate_primes() -> Tuple[int, int]:
    primes = []
    for i in range(10000, 100000):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)

    return p, q


# Calculate greatest common divisor of two numbers
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Calculate modular inverse of a number
def mod_inv(a: int, m: int) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Calculate Euler's totient function of n
def euler_totient(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


# Generate public and private keys
def generate_keys() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    p, q = generate_primes()
    n = p * q
    phi_n = euler_totient(p, q)

    # Choose a random integer e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Calculate the modular inverse of e modulo phi_n
    d = mod_inv(e, phi_n)

    # Return public and private keys
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


# Encrypt a message using public key
def encrypt(public_key: Tuple[int, int], message: str) -> int:
    e, n = public_key
    


# Decrypt a ciphertext using private key
def decrypt(private_key: Tuple[int, int], ciphertext: int) -> str:
    d, n = private_key
    m = pow(ciphertext, d, n)
    message = ''
    while m > 0:
        message = chr(m & 0x7f) + message
        m >>= 7
    return message

# Test the RSA algorithm with random data
if __name__ == '__main__':
    # Generate public and private keys
    public_key, private_key = generate_keys()
    print('Public key:', public_key)
    print('Private key:', private_key)

    # Test encryption and decryption
    message = 'Hello World'
    message_encode = [ord(ch) for ch in message]
    
    # (m ^ e)mod n = c
    ciphertext =[pow(ch,e,n) for ch in message_encode for e, n in public_key ]
    print(ciphertext)

    # print('Original message:', message)
    # ciphertext = encrypt(public_key, message)
    # print('Ciphertext:', ciphertext)
    # decrypted_message = decrypt(private_key, ciphertext)
    # print('Decrypted message:', decrypted_message)