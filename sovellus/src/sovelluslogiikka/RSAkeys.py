from generate_keys import key_generator

class rsa_keys:

    def __init__(self):
        self.public_key = None
        self.private_key = None

generate = key_generator(1024)
generate.generate_keys()