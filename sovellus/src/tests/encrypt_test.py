import unittest
from sovelluslogiikka.encrypt import encrypt
from sovelluslogiikka.generate_keys import key_generator
from sovelluslogiikka.RSAkey import rsa_key
from sovelluslogiikka.smallprimes import small_primes

class TestEncrypter(unittest.TestCase):
    def setUp(self):
        self.generator = key_generator(2048, small_primes, rsa_key)
        self.generator.generate_keys()
        self.msg = "Tämä on testi viesti."
    
    def test_encryption(self):
        encrypted_msg = encrypt().encrypt(self.msg, self.generator.pub_key)
        self.assertEqual(encrypted_msg == self.msg, False)
        self.assertEqual(type(encrypted_msg), int)
    
    def test_string_to_bytes(self):
        in_bytes = encrypt().string_to_bytes(self.msg)
        self.assertEqual(type(in_bytes), bytes)

    def test_bytes_to_int(self):
        in_bytes = encrypt().string_to_bytes(self.msg)
        in_int = encrypt().bytes_to_int(in_bytes)
        self.assertEqual(type(in_int), int)


