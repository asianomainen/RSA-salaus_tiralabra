# Toteutusdokumentti

Toteutusdokumentti RSA-salauksen implementoinnille pythonia käyttäen.

## Ohjelman yleisrakenne

Ohjelman sovelluslogiikka koostuu viidestä luokasta:

1. `key_generator`
   - Luokka RSA-avaimen luomiseen
   - Konstruktori:
      - Saa parametreiksi avaimen pituuden lisäksi `small_primes` ja `rsa_key` -luokat
   - Metodit:
      - `generate_keys`
          - Luo ja tallentaa RSA-avaimet
      - `generate_number`
          - Luo parametrin n mittaisen satunnaisen luvun
      - `compute_lambdan`
          - Laskee Carmichaelin funktion arvon parametrien tulolla
      - `generate_prime_numbers`
          - Luo kaksi alkulukua, siten että p!=q
      - `is_prime`
          - Tarkistaa onko annettu luku alkuluku
      - `screening`
          - Alustava tarkistus alkuluku ehdokkaalle
      - `miller_rabin`
          - Tekee halutulle luvulle Miller-Rabin alkuluku testin k kertaa.

2. `rsa_key`
    - Luokka RSA-avaimen tallentamiseen
    - Konstruktori:
        - Saa parametriksi avaimen modulon ja eksponentin
    - Metodit:
        - `get_modulus`
           - Plauttaa avaimen modulon
        - `get_exponent`
           - Palauttaa avaimen eksponentin


3. `small_primes`
    - Luokka pienten alkulukujen generoimiseen
    - Konstruktori:
        - Saa parametriksi luvun mihin asti alkulukuja generoidaan
    - Metodit:
        - `generate_list`
            - Palauttaa listan alkuluvuista


4. `encrypt`
    - Luokka viestin salaamiseen
    - Metodit:
        - `encrypt`
            - Salaa viestin
        - `text_to_bytes`
            - Muuntaa viestin tavuiksi
        - `bytes_to_int`
            - Muuntaa tavut luvuksi

5. `decrypt`
    - Luokka salatun viestin purkamiseen
    - Metodit:
        - `decrypt`
            - Purkaa salatun viestin
        - `int_to_bytes`
            - Muuntaa luvun tavuiksi
        - `bytes_to_text`
            - Muuntaa tavut tekstiksi
           
## Suorituskykyvertailu

Suorituskykyvertailu on tehty generoimalla eri pituisia avainpareja ja ottamalla keskiarvo kymmenestä suorituskerrasta.

Avaimen pituus bitteinä | Keskiarvo (10 suorituskertaa)|
----|----------|
1024 | 0,078s
2048 | 0,702s
4096 | 8,785s

