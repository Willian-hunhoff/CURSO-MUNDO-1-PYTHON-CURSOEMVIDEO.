@echo off

if not exist Executaveis mkdir Executaveis

for /R %%f in (*.py) do (
    echo Convertendo %%~nxf...
    pyinstaller --onefile --distpath Executaveis "%%f"
)

echo.
echo Conversao concluida!
pause