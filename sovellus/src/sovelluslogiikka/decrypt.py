class decrypt:

    def decrypt(self, msg, key):
        decrypted = pow(msg, key.get_exponent(), key.get_modulus())
        in_bits = self.int_to_bits(decrypted)
        in_text = self.bits_to_text(in_bits)
        return in_text
    
    def int_to_bits(self, msg):
        return msg.to_bytes(2048, "big")
    
    def bits_to_text(self, msg):
        return msg.decode()
