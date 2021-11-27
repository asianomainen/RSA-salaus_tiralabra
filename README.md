# RSA-salaus

Helsingin yliopiston Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/maarittelydukumentti.md)
- [Testausdokumentti](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/toteutusdokumentti.md)

## Viikkoraportit

- [Viikko 1](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti1.md)
- [Viikko 2](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti2.md)
- [Viikko 3](https://github.com/ItsTuukka/RSA-salaus_tiralabra/blob/master/dokumentaatio/viikkoraportti3.md)

## Komentorivikomennot

#### Ohjelman voi suorittaa komennolla 

```
poetry run invoke start
```
(ei vielä suorita mitään)

#### Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

#### Testikattavuusraportin saa luotua komennolla

```
poetry run invoke coverage-report
```

Raportti generoituu sovellus/htmlcov/index.html tiedostoon.

#### Pylint tarkistus komennolla

```
poetry run invoke lint
```
