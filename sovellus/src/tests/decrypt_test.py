import unittest
from sovelluslogiikka.decrypt import decrypt
from sovelluslogiikka.encrypt import encrypt
from sovelluslogiikka.generate_keys import key_generator
from sovelluslogiikka.RSAkey import rsa_key
from sovelluslogiikka.smallprimes import small_primes

class TestDecrypt(unittest.TestCase):
    def setUp(self):
        self.generator = key_generator(2048, small_primes, rsa_key)
        self.generator.generate_keys()
        self.msg = "Tämä on testi viesti."
        self.encrypted_msg = encrypt().encrypt(self.msg, self.generator.pub_key)
    
    def test_decryption(self):
        decrypted_msg = decrypt().decrypt(self.encrypted_msg, self.generator.pvt_key)
        self.assertEqual(decrypted_msg, self.msg)
    
    def test_int_to_bytes(self):
        in_bytes = decrypt().int_to_bytes(self.encrypted_msg)
        self.assertEqual(type(in_bytes), bytes)

    def test_bytes_to_string(self):
        in_bytes = decrypt().int_to_bytes(self.encrypted_msg)
        in_string = decrypt().bytes_to_string(in_bytes)
        self.assertEqual(type(in_string), str)