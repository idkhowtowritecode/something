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

    :: Delete the original .dat file
    del "%%f"
    echo Deleted %%f
)

:: Zip the directory using PowerShell
echo Zipping the directory...
powershell Compress-Archive -Path "%destDir%\*" -DestinationPath "%destDir%.zip"

:: Check if the zip operation was successful
if exist "%destDir%.zip" (
    echo Zip operation successful.
    
    :: Delete the directory
    echo Deleting the directory...
    rmdir /s /q "%destDir%"
    
    :: Check if the directory was deleted successfully
    if not exist "%destDir%" (
        echo Directory deleted successfully.
    ) else (
        echo Failed to delete the directory.
    )
) else (
    echo Failed to zip the directory.
)

endlocal
