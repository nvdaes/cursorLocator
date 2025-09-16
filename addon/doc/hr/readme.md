# Lokator kursora (Cursor Locator) #

* Autori: Noelia Ruiz Martínez, Sergio Gómez Codina.

Ovaj dodatak omogućuje saznati položaj kursora sustava u odnosu na početak
trenutačnog retka, tijekom tipkanja za dodavanje teksta u dokumente ili
višeredne kontrole.

Ova značajka ovisi o vizualnom izgledu aplikacija. Stoga će možda biti
potrebno deaktivirati prilagođavanje redaka ili konfigurirati dodatak za
drugačije programe.

## Lokator kursora – postavke ##

Ova ploča dostupna je putem NVDA izbornika, podizbornik Postavke, dijaloški
okvir Postavke.

Pruža sljedeće opcije:

* Izvijesti o duljini retka: upiši ili odaberi duljinu retka (broj znakova
  između 0 i 600), koja će se najaviti visokim tonom kad se
  dosegne. (Standardna vrijednost je 80 znakova).
* Maksimalan broj zvučnih signala za obavijest o početku retka: upiši ili
  odaberi vrijednost između 0 i 600. Standardna vrijednost je 0.
* Maksimalan broj zvučnih signala za obavijest o kraju retka: upiši ili
  odaberi vrijednost između 0 i 600. Standardna vrijednost je 0.
* Visina zvuka za početak retka: upiši ili odaberi vrijednost između 20 i
  20000. (Standardna vrijednost je 400 herca).
* Trajanje zvuka za početak retka: upiši ili odaberi vrijednost između 20 i
  2000. (Standardna vrijednost je 50 milisekunda).
* Testiranje zvuka za početak retka: pritisni ovaj gumb za testiranje
  konfiguriranog zvuka za početak retka.
* Visina zvuka za kraj retka: upiši ili odaberi vrijednost između 20 i
  20000. (Standardna vrijednost je 1000 herca).
* Trajanje zvuka za kraj retka: upiši ili odaberi vrijednost između 20 i
  2000. (Standardna vrijednost je 50 milisekunda).
* Testiranje zvuka za kraj retka: pritisni ovaj gumb za testiranje
  konfiguriranog zvuka za kraj retka.

## Naredbe ##

Geste se mogu promijeniti u sljedeće naredbe putem NVDA izbornika,
podizbornik Postavke, dijaloški okvir za ulazne geste:

* NVDA+kontrol+šift+l: Kad je moguće, izvještava o duljini trenutačnog retka
  (kategorija kursora sustava).
* Nije dodijeljeno: Prikazuje dijaloški okvir postavki za „Lokator kursora”
  (kategorija konfiguracije).

## Promjene u verziji 3.0 ##
* Kompatibilno s NVDA čitačem 2023.1.

## Promjene u verziji 2.0 ##
* Dodana je mogućnost ponavljanja obavijesti kad se dosegne kraja i početka
  retka.
* Dodana je podrška za Office dokumente i Notepad na sustavu Windows 11.

## Promjene u verziji 1.0 ##
* Prva verzija

[[!tag dev stable]]
