@echo off
setlocal enabledelayedexpansion

:: Prompt the user for the destination directory
set /p "destDir=Enter the directory to save the log files: "

:: Check if the directory exists, if not create it
if not exist "%destDir%" (
    mkdir "%destDir%"
)

:: Loop through all .dat files in the current directory and its subdirectories
for /r %%f in (*.dat) do (
    :: Extract the file name without extension
    set "filename=%%~nf"
    
    :: Run the loganalyse.exe command to transform the .dat file into a .txt file in the specified directory
    loganalyse.exe "%%f" > "%destDir%\%%~nf.txt"
    echo Transformed %%f to %destDir%\%%~nf.txt
)

endlocal
