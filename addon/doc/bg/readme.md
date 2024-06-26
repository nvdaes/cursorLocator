# Локатор на курсора (Cursor Locator) #

* Автори: Noelia Ruiz Martínez, Sergio Gómez Codina.

Тази добавка дава възможност да се узнава позицията на системната карета
спрямо началото на текущия ред, докато пишете, за да добавите текст в
документи или многоредови контроли.

Тази функция зависи от изгледа на приложенията. Следователно може да се
наложи да деактивирате нагласянето на реда или да конфигурирате добавката за
различни програми.

## Настройки на "Локатор на курсора" ##

Този панел е достъпен от менюто на NVDA -> подменю "Настройки" -> диалоговия
прозорец "Настройки".

Предоставя следните опции:

* Докладвай дължината на реда: Можете да въведете или изберете дължина на
  реда (брой знаци между 0 и 600), която ще бъде докладвана с висок тон,
  когато бъде достигната. Стойността по подразбиране е 80 знака.
* Максимален брой звукови сигнали за известие за началото на реда: Можете да
  въведете или изберете стойност между 0 и 600. Стойността по подразбиране е
  0.
* Максимален брой звукови сигнали за известие за края на реда: Можете да
  въведете или изберете стойност между 0 и 600. Стойността по подразбиране е
  0.
* Височина на звука за начало на реда: Можете да въведете или изберете
  стойност между 20 и 20000. Стойността по подразбиране е 400 херца.
* Дължина на звука за начало на реда: Можете да въведете или изберете
  стойност между 20 и 2000. Стойността по подразбиране е 50 милисекунди.
* Изпробвай звука за начало на реда: Натиснете този бутон, за да изпробвате
  конфигурирания звук за начало на реда.
* Височина на звука за край на реда: Можете да въведете или изберете
  стойност между 20 и 20000. Стойността по подразбиране е 1000 херца.
* Дължина на звука за край на реда: Можете да въведете или изберете стойност
  между 20 и 2000. Стойността по подразбиране е 50 милисекунди.
* Изпробвай звука за край на реда: Натиснете този бутон, за да изпробвате
  конфигурирания звук за край на реда.

## Команди ##

Можете да промените жестовете към следните команди от менюто на NVDA ->
подменю Настройки -> диалоговия прозорец "Жестове на въвеждане":

* NVDA+Control+Shift+L: Когато е възможно, докладва дължината на текущия ред
  (категория "Каретка").
* Не е зададено: Показва диалоговия прозорец за настройки на "Локатор на
  курсора" (категория "Настройки").

## Промени във версия 3.0 ##
* Добавката е съвместима с NVDA 2023.1.

## Промени във версия 2.0 ##
* Добавена е възможност за повтаряне на известията при достигане на края и
  началото на реда.
* Добавена е поддръжка за документи на Office и Notepad в Windows 11.

## Промени във версия 1.0 ##
* Първо издание

[[!tag dev stable]]
