@ECHO OFF

:: #######################################################
:: Environment Definition
:: #######################################################
set PYTHON_FOLDER=D:\python\python_3_10_0
:: #######################################################

set "Current_Dir=%cd%\"
if "%Current_Dir:~-1%" == "\" (
    set "Current_Dir1=%Current_Dir:~0,-1%"
)

for %%f in ("%Current_Dir1%") do set "lastfolder=%%~nxf"

if %lastfolder% == scripts (

    :: Create venv
    echo y |%PYTHON_FOLDER%\python.exe -m venv ..\.venv

    :: Need to add this var into the activate.bat before.
    :: echo set "TCL_LIBRARY=%PYTHON_FOLDER%\tcl\tk8.6" >> ..\.venv\Scripts\activate.bat  

    :: activate the env
    call ..\.venv\Scripts\activate.bat    

    :: Display installed pkg
    pip list

    pip install -r ..\requirements.txt

    echo.
    echo Install pkg completed.
    echo.

    pip list

) else (
    echo To run, this file must be located in the directory named "scripts".
    pause
    exit 
)