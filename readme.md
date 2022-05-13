# Cursor Locator #
* Authors: Noelia Ruiz Martínez, Sergio Gómez Codina.
* Download [stable version][1] (compatible with NVDA 2022.1 and beyond).

This add-on makes possible to know the position of the system caret respect to the start of the current line, while typing to add text in documents or multiline controls.

This feature deppends on the visual appearance of applications. Therefore, you may need to disable line adjustment or configure the add-on for different programs.

## Cursor Locator settings ##

This panel is available from NVDA's menu, Preferences submenu, Settings dialog.

It provides the following options:

* Report start of line: When this control is checked, a low tone will announce if the caret is at the start of the current line while text is been added. (Checked by default).
* Report line length: You can type or choose a line length (number of characters between 0 and 600), which will be announced by a hight tone when it's reached. (The default value is 80 characters).
* Pitch of sound for start of line: You can type or select a value between 20 and 20000. (The default value is 400 hertzs).
* Length of sound for start of line: You can type or select a value between 20 and 2000. (The default value is 50 milliseconds).
* Test sound for start of line: Press this button to test the configured sound for start of line.
* Pitch of sound for end of line: You can type or select a value between 20 and 20000. (The default value is 1000 hertzs).
* Length of sound for end of line: You can type or select a value between 20 and 2000. (The default value is 50 milliseconds).
* Test sound for end of line: Press this button to test the configured sound for end of line.

## Commands ##

You can modify the gestures to the following commands trought the NVDA's menu, Preferences submenu, Input gestures dialog:

* NVDA+control+shift+l: When possible, reports the lenght of the current line (System caret category).
* Not assigned: Shows the Cursor Locator settings dialog (Config category).

## Changes for 1.0 ##
* Initial version

[1]: https://addons.nvda-project.org/files/get.php?file=cursorLocator
