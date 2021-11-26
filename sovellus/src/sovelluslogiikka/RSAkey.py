class rsa_key:

    def __init__(self, mod, exponent):
        self.modulus = mod
        self.exponent = exponent
    
    def get_modulus(self):
        return self.modulus
    
    def get_exponent(self):
        return self.exponent