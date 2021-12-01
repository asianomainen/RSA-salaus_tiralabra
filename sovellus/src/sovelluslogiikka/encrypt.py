class encrypt:

    def encrypt(self, msg, key):
        in_bits = self.text_to_bits(msg)
        in_int = self.bits_to_int(in_bits)
        return pow(in_int, key.get_exponent(), key.get_modulus())

    def text_to_bits(self, msg):
        return msg.encode()

    def bits_to_int(self, msg):
        return int.from_bytes(msg, "big")

