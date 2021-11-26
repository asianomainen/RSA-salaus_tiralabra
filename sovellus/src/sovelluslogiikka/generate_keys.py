import random
import math
from smallprimes import small_primes
from RSAkey import rsa_key
from timeit import default_timer as timer


class key_generator:

    """Luokka vastaa RSA-avainten luomisesta.

    Attributes:
        small_primes: Lista pienistä alkuluvuista.
        lenght: Avainten luomiseen käytettyjen alkulujenlukujen pituus biteissä. 
        e: Osa julkista-avainta.
    """

    def __init__(self, length):
        """Luokan konstruktori.

        Args: 
            lenght: Avainten pituus biteissä.
        """

        sm = small_primes(500)
        self.small_primes = sm.prime_list
        self.length = length
        self.e = 65537
        self.pub_key = None
        self.pvt_key = None

    def generate_keys(self):
        """Luo ja tallentaa RSA-avainparin.
        """

        p, q = self.generate_prime_numbers()
        modulus = p*q
        lambdan = self.compute_lambdan(p-1, q-1)
        exponent = pow(self.e, -1, lambdan)
        self.pub_key = rsa_key(modulus, self.e)
        self.pvt_key = rsa_key(modulus, exponent)
    
    def generate_number(self, n):
        """Luo n-bittiä pitkän luvun.

        Args: 
            n: Integer, luvun pituus biteissä

        Returns: 
            Integer, jonka pituus on n bittiä.
        """

        return random.getrandbits(n)
    
    def compute_lambdan(self, p, q):
        """Laskee Carmichaelin funktion arvolla p*q.

        Args:
            p: Integer, löydetty alkuluku - 1.
            q: Integer, löydetty alkuluku - 1.
        
        Returns:
            Integer, joka on Carmichaelin funktion arvolla p*q.
        """

        return abs(p*q) // math.gcd(p, q)

    def generate_prime_numbers(self):
        """Luo alkuluvut p ja q, niin että p != q.

        Returns:
            Tuple, joka sisältää löydetyt alkuluvut.
        """

        while True:
            p = self.generate_number(self.length//2)
            if p % 2 == 0:
                continue
            if self.is_prime(p):
                break
        while True:
            q = self.generate_number(self.length//2)
            if q % 2 == 0 or q == p:
                continue
            if self.is_prime(q):
                break
        return (p, q)

    def is_prime(self, n):
        """Tarkistaako onko luku alkuluku.

        Args:
            n: Integer, jota halutaan testata.

        Returns: 
            True, jos luku on alkuluku.
        """

        if not self.screening(n):
            return False
        if not self.miller_rabin(n, 40):
            return False
        return True

    def screening(self, n):
        """Tekee alustavan tarkistuksen alkuluku ehdokkaalle, jakamalla sitä pienillä alkuluvuilla.

        Args:
            n: Integer, jota halutaan testata.
        
        Returns:
            True, jos luku ei ole jaettavissa tasan millään pienellä alkuluvulla
        """

        for prime in self.small_primes:
            if n % prime == 0:
                return False
        return True

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
            a = random.randint(2, n-2)
            if math.gcd(n, a) != 1:
                return False
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


if __name__ == '__main__':
    start = timer()
    generate = key_generator(2048)
    generate.generate_keys()
    end = timer()
    print(end - start)
