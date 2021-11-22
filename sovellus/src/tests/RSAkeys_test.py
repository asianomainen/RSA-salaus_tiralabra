import unittest
from sovelluslogiikka.RSAkeys import rsa_keys

class TestRSA(unittest.TestCase):
    def setUp(self):
        self.rsa = rsa_keys()
        self.big_prime = 982451653
        self.big_composite = 124251499
    
    def test_is_prime(self):
        self.assertEqual(True, self.rsa.is_prime(self.big_prime))
        self.assertEqual(False, self.rsa.is_prime(self.big_composite))

    def test_miller_rabin(self):
        self.assertEqual(True, self.rsa.miller_rabin(self.big_prime, 40))
        self.assertEqual(False, self.rsa.miller_rabin(self.big_composite, 40))
    
    def test_screening(self):
        self.assertEqual(True, self.rsa.screening(self.big_prime))
        self.assertEqual(False, self.rsa.screening(self.big_composite))
