# Testausdokumentti

## Yksikkötestaus

Yksikkötestaus suoritetaan automaattisesti unittestiä käyttäen.

### Sovelluslogiikka

Pienistä alkuluovuista vastaavaa `small_primes` -luokkaa testataan omassa luokassaan. `TestSmallprimes` -testiluokka vertaa `small_primes` -luokan `generate_list` -metodin tuottamaa listaa ja vertaa sitä tunnettuun listaan alkuluvuista.

Julkisen ja yksityisen avaimen hallinnoinnista ja generoimisesta vastaava `rsa_keys` -luokka testataan omassa luokassaan, mutta tämä myös vaatii `small_primes` -luokan attribuutteja. `TestRSA` -testiluokka testaa alkuluvun etsimiseen tarkotettuja metodeja tunnetulla alkuluvulla sekä tunnetullu yhdistetyllä luvulla.

## Testikattavuus

Testien haarautumakattavuus on 94%. Raportista on jätetty ulkopuolelle käyttöliittymän koodi.

![coverage](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/kuvat/rsa_coverage.png)

## Järjestelmätestaus

(tulossa)

## Suorituskykytestaus

(tulossa)

## Testien suorittaminen

Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

Testikattavuusraportin saa luotua komennolla 

```
Raportti generoituu sovellus/htmlcov/index.html tiedostoon.

