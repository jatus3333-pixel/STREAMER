@echo off
REM Fixes "PyInstaller does not include a pre-compiled bootloader" for auto-py-to-exe
cd /d "%~dp0"

where python >nul 2>&1 || (
  echo [ERROR] python not found in PATH.
  exit /b 1
)

echo [INFO] Reinstalling PyInstaller (restores runw.exe bootloaders)...
python -m pip uninstall pyinstaller -y 2>nul
python -m pip install pyinstaller --no-cache-dir --force-reinstall --no-warn-script-location
if errorlevel 1 (
  echo.
  echo [WARN] pip reported errors. Bootloaders may still be OK - checking...
)

python -c "import os,PyInstaller; p=os.path.join(os.path.dirname(PyInstaller.__file__),'bootloader','Windows-64bit-intel','runw.exe'); exit(0 if os.path.isfile(p) else 1)"
if errorlevel 1 (
  echo [ERROR] Bootloader still missing. Install Python from https://www.python.org/downloads/
  echo        ^(not Microsoft Store^), then run this script again.
  exit /b 1
)

echo [OK] PyInstaller bootloaders are present.
echo.
echo Open auto-py-to-exe with:
echo   python -m auto_py_to_exe
echo.
echo Or build this project with:
echo   build.cmd
pause
