# Testausdokumentti

## Yksikkötestaus

Yksikkötestaus suoritetaan automaattisesti unittestiä käyttäen.

### Sovelluslogiikka

Pienistä alkuluvuista vastaavaa `small_primes` -luokkaa testataan omassa luokassaan. `TestSmallprimes` -testiluokka vertaa `small_primes` -luokan `generate_list` -metodin tuottamaa listaa ja vertaa sitä tunnettuun listaan alkuluvuista.

Julkisen ja yksityisen avaimen hallinnoinnista ja generoimisesta vastaava `rsa_keys` -luokka testataan omassa luokassaan. `TestRSA` -testiluokka testaa alkuluvun etsimiseen tarkotettuja metodeja tunnetulla alkuluvulla sekä tunnetullu yhdistetyllä luvulla.

## Testikattavuus

Testien haarautumakattavuus on 94%. Raportista on jätetty ulkopuolelle käyttöliittymän koodi.

![coverage](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/kuvat/rsa_coverage.png)

## Järjestelmätestaus

Sovellusta testattu järjestelmätasolla manuaalisesti, eikä ongelmia ole havaittu.

## Suorituskykytestaus

Suorituskykyä on testattu generoimalla eri pituisia avaimia ja ottamalla keskiarvo kymmenestä suorituskerrasta. Sovelluksessa käytetään avaimen pituutena 2048 bittiä, joka on tällä hetkellä suositeltu pituus RSA-avaimelle. 

Avaimen pituus bitteinä | Keskiarvo (10 suorituskertaa)|
----|----------|
1024 | 0,078s
2048 | 0,702s
4096 | 8,785s

## Testien suorittaminen

Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

Testikattavuusraportin saa luotua komennolla 

```
Raportti generoituu sovellus/htmlcov/index.html tiedostoon.

