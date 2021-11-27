# from generate_keys import key_generator 
# kg = key_generator(2048)
# kg.generate_keys()
# n = kg.pub_key.get_modulus()
# e = kg.pub_key.get_exponent()
# d = kg.pvt_key.get_exponent()
# msg = "Tämä on testi"
# msg_bits = msg.encode()
# print(msg_bits)
# lukuna = int.from_bytes(msg_bits, "big")
# print(lukuna)
# encrypted = pow(lukuna, e, n)
# decrypted = pow(encrypted, d, n)
# print(decrypted)
# purettu = decrypted.to_bytes(len(str(lukuna)), "big")
# purettu = purettu.decode()
# print(purettu)
"""logiikka encode/decode toiminnoille"""
