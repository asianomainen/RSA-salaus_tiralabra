import random


class rsa_keys:

    """Luokka vastaa RSA-avainten luomisesta.

    Attributes:
        public_key
        private_key
    """

    def __init__(self):
        """Luokan konstruktori.
        """
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        """Luo RSA-avainparin

        Returns:
            RSA-avainparin
        """

        p, q = self.generate_prime_numbers()

    def generate_prime_numbers(self):
        """Luo alkuluvut p ja q, niin että p*q >= 2048 bittiä ja p != q.

        Returns:
            Alkulukuparin.
        """

        while True:
            p, q = random.getrandbits(1030), random.getrandbits(1030)
            if p == q or p % 2 == 0 or q % 2 == 0:
                continue
            if self.is_prime(p) and self.is_prime(q):
                break
        return (p, q)

    def is_prime(self, n):
        """Tarkistaako onko luku alkuluku.

        Args:
            n: Integer, jota halutaan testata

        Returns: 
            True, jos luku on alkuluku.
        """

        if self.miller_rabin(n, 40):
            return True
        return False

    def miller_rabin(self, n, k):
        """Tekee halutulle luvulle n Miller-Rabin alkuluku testin k kertaa.
        Todennäköisyys, että testin hyväksymä luku ei ole alkuluku on korkeintaan 4**-k (k=40).

        Args:
            n: Integer, jota halutaan testata.
            k: Integer, testin iteraatioiden määrä.

        Returns: 
            True, jos luku on hyvin suurella todennäköisyydellä alkuluku.
        """

        r, d = 0, n-1
        while d % 2 == 0:
            r += 1
            d = d // 2

        for _ in range(k):
            a = random.randint(2, n-1)
            x = pow(a, d, n)
            if x == 1 or x == n-1:
                continue
            for _ in range(r-1):
                x = pow(x, 2, n)
                if x == n-1:
                    break
            else:
                return False
        return True
