import random
import math

# Generate 5-digit prime numbers p and q
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number% i == 0:
            return False
    return True

def generate_primes(min_val, max_val):
    prime = random.randint(min_val, max_val)
    while not is_prime(prime):
        prime = random.randint(min_val, max_val)
    return prime

# Calculate greatest common divisor of two numbers
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Calculate modular inverse of a number
def mod_inv(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError('No modular inverse found')

p, q = generate_primes(10000,100000), generate_primes(10000,100000)

while p == q:
    q = generate_primes(10000,100000)
    
n = p * q
# Calculate Euler's totient function of n
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n - 1)
while math.gcd (e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)


d = mod_inv(e, phi_n)

print("Public key: ", e)
print("Private key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p: ", p)
print("q: ", q)


message = 'Hello World'

message_encode = [ord(ch) for ch in message]
    
# (m ^ e)mod n = c
ciphertext =[pow(ch,e,n) for ch in message_encode]

print(ciphertext)

message_decode = [chr(pow(ch,d,n)) for ch in ciphertext]
decrypted = "".join(chr(ch) for ch in message_decode)

print(decrypted)