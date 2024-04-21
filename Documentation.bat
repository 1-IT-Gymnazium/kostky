@echo off
setlocal

:: Nastavte relativní cestu k souboru index.html
set FILEPATH=docs\_build\html\index.html

:: Otevřete soubor index.html
start "" "%FILEPATH%"

endlocal
