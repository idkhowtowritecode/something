@echo off
setlocal enabledelayedexpansion

:: Initialize an array
set "fileArray="

:: Loop through all .dat files in the current directory and its subdirectories
for /r %%f in (*.dat) do (
    :: Add the file name to the array
    set "fileArray=!fileArray! %%~nxf"
)

:: Print the array to the console
for %%i in (!fileArray!) do (
    echo %%i
)

endlocal
