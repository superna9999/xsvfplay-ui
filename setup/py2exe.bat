::-----------------------------------------------------------------------------
:: Wrapper script to build a Windows executable from a Python script
:: You may need to define the PYTHON environment variable so that it points to
:: a valid python executable
::
:: @pre distutils and py2exe tools are required
::
:: This script should be started from the setup directory, and the name of the
:: python script to package should be provided as the first argument, such as
::   C:\sdk\trunk\host\bin\setup> py2exe.bat neoloader
::-----------------------------------------------------------------------------
@echo off

set PYTHON=C:\Python26\python.exe

if "n%1" == "n" (echo Usage: py2exe.bat script
                 goto end)
if not exist "..\%~n1.py" (echo Usage: ..\%~n1.py script does not exist
                           goto end)
if not exist "%~n1.py" (echo Usage: %~f1.py installation script does not exist
                        goto end)

set OLDPATH=%PATH%
set PATH=%SystemRoot%\system32
pushd ..
%PYTHON% setup\%~n1.py py2exe
echo.
if exist build (del /S /Q build > NUL
                rmdir /S /Q build > NUL)
popd ..
set PATH=%OLDPATH%

:end

