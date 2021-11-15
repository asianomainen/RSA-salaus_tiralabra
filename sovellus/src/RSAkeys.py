import random
import math
from smallprimes import small_primes
from timeit import default_timer as timer


class rsa_keys:

    """Luokka vastaa RSA-avainten luomisesta.

    Attributes:
        public_key
        private_key
        small_primes: Lista pienistä alkuluvuista.
        lenght: Avainten luomiseen käytettyjen lukujen pituus biteissä.
                Tässä tapauksessa 1024 bittiä, mikä vastaa 2048 bittiä pitkää avainta.
                
    """

    def __init__(self):
        """Luokan konstruktori.
        """

        sm = small_primes()
        self.public_key = None
        self.private_key = None
        self.small_primes = sm.prime_list
        self.length = 1024

    def generate_number(self, n):
        """Luo n-bittiä pitkän luvun.

        Args: 
            n: Integer, luvun pituus biteissä

        Returns: 
            Integer, jonka pituus on n bittiä.
        """

        return random.getrandbits(n)

    def generate_keys(self):
        """Luo RSA-avainparin.

        Returns:
            RSA-avainparin.
        """

        p, q = self.generate_prime_numbers()
        print("alkuluvut löydetty")

    def generate_prime_numbers(self):
        """Luo alkuluvut p ja q, niin että p != q.

        Returns:
            Alkulukuparin.
        """

        while True:
            p = self.generate_number(self.length)
            if p % 2 == 0:
                continue
            if self.is_prime(p):
                break
        while True:
            q = self.generate_number(self.length)
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
    
    # def screening(self, n): ///en ole saanut toimimaan tehostettua versiota
    #     mod_list = []
    #     for i in range(len(self.small_primes)):
    #         mod_list.append(pow(n, 1, self.small_primes[i]))
    #     for i in range(len(mod_list)):
    #         if mod_list[i] == 0:
    #             return False

    def screening(self, n):
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
    keys = rsa_keys()
    keys.generate_keys()
    end = timer()
    print(end - start)
