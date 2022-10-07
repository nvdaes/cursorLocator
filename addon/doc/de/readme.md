# Cursor ermitteln #
* Autoren: Noelia Ruiz Martínez, Sergio Gómez Codina.
* [Stabile Version herunterladen][1] (kompatibel mit NVDA 2022.1 und neuer.

Mit dieser Erweiterung können Sie die Position des System-Cursors in Bezug
auf den Anfang der aktuellen Zeile ermitteln, während der Eingabe, um Text
in Dokumente oder mehrzeilige Steuerelemente einzufügen.

Diese Funktion wirkt sich auf das Erscheinungsbild von Anwendungen
aus. Daher müssen Sie möglicherweise die Zeilenanpassung deaktivieren oder
die Erweiterung für verschiedene Programme konfigurieren.

## Einstellungen für die Cursor-Ermittlung ##

Dieses Panel ist über das NVDA-Menü in den Einstellungen verfügbar.

Es gibt die folgenden Optionen:

* Zeilenlänge melden: Sie können eine Zeilenlänge (Anzahl der Zeichen
  zwischen 0 und 600) eingeben oder auswählen, die bei Erreichen mit einem
  hohen Ton mitgeteilt wird. Der Standardwert ist 80 Zeichen.
* Maximale Anzahl von Signaltönen für die Benachrichtigung über den Anfang
  einer Zeile: Sie können einen Wert zwischen 0 und 600 eingeben oder
  auswählen. Der Standardwert ist 0.
* Maximale Anzahl von Signaltönen für die Benachrichtigung über das Ende der
  Zeile: Sie können einen Wert zwischen 0 und 600 eingeben oder
  auswählen. Der Standardwert ist 0.
* Tonhöhe für den Anfang der Zeile: Sie können einen Wert zwischen 20 und
  20000 eingeben oder auswählen. (Der Standardwert ist 400 Hertz).
* Tonlänge am Anfang der Zeile: Sie können einen Wert zwischen 20 und 2000
  eingeben oder auswählen. (Der Standardwert ist 50 Millisekunden).
* Testton für Zeilenanfang: Drücken Sie diese Taste, um den konfigurierten
  Ton für den Anfang der Zeile zu testen.
* Tonhöhe für das Ende einer Zeile: Sie können einen Wert zwischen 20 und
  20000 eingeben oder auswählen. (Der Standardwert ist 1000 Hertz).
* Tonlänge für das Ende der Zeile: Sie können einen Wert zwischen 20 und
  2000 eingeben oder auswählen. (Der Standardwert ist 50 Millisekunden).
* Testton für Zeilenende: Drücken Sie diese Taste, um den konfigurierten Ton
  für das Ende der Zeile zu testen.

## Befehle ##

Sie können den Tastenbefehl mit den folgenden Befehlen über das NVDA-Menü,
Untermenü Einstellungen, Dialogfeld für die Tastenbefehle ändern:

* NVDA+Strg+Umschalt+L: Wenn möglich, wird die Länge der aktuellen Zeile
  angezeigt (Kategorie System-Cursor).
* Nicht zugewiesen: Zeigt den Einstellungsdialog für den Cursor Locator an
  (Konfigurationskategorie).


## Änderungen in 2.0 ##
* Es besteht die Möglichkeit, Benachrichtigungen zu wiederholen, wenn das
  Ende oder der Anfang einer Zeile erreicht wird.
* Unterstützung für Office-Dokumente und Notepad unter Windows 11
  hinzugefügt.

## Änderungen in 1.0 ##
* Erste Version

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cursorLocator
