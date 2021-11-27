from sovelluslogiikka.RSAkey import rsa_key
from sovelluslogiikka.smallprimes import small_primes
from sovelluslogiikka.generate_keys import key_generator

while True:
    print("0: lopeta")
    print("1: generoi RSA-avaimet")
    choice = int(input())
    if choice == 1:
        length = int(input("Anna avainten pituus (suositus 2048): "))
        kg = key_generator(length, small_primes, rsa_key)
        kg.generate_keys()
        print("Avaimet luotu")
        text = str(input("Anna salattava viesti: "))
        break
    else:
        break
