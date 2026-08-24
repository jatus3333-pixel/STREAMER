@echo off
setlocal enabledelayedexpansion

REM Build app.py -> dist\app.exe (single-file, no console)
cd /d "%~dp0"

set "PY="
where py >nul 2>&1 && set "PY=py"
if not defined PY (
  where python >nul 2>&1 && set "PY=python"
)
if not defined PY (
  echo [ERROR] Python not found. Install Python 3.10+ and add it to PATH.
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo [INFO] Creating virtual environment...
  %PY% -m venv .venv || exit /b 1
)

set "VENV_PY=%CD%\.venv\Scripts\python.exe"

echo [INFO] Installing build dependencies...
"%VENV_PY%" -m pip install ^
  pyinstaller flask flask-cors psutil pymem keyboard pynput pywin32 requests
if errorlevel 1 (
  echo [WARN] pip install failed - recreating .venv ...
  rmdir /s /q ".venv" 2>nul
  %PY% -m venv .venv || exit /b 1
  set "VENV_PY=%CD%\.venv\Scripts\python.exe"
  "%VENV_PY%" -m pip install ^
    pyinstaller flask flask-cors psutil pymem keyboard pynput pywin32 requests ^
    || exit /b 1
)

if not exist "app.py" (
  echo [ERROR] Entry file not found: app.py
  exit /b 1
)

for %%F in (cimgui.dll AotBst.dll Client.dll index.html login.html) do (
  if not exist "%%F" (
    echo [WARN] Missing: %%F
  )
)

echo [INFO] Building dist\app.exe ...
"%VENV_PY%" -m PyInstaller --noconfirm --clean app.spec || exit /b 1

if not exist "dist\app.exe" (
  echo [ERROR] Build finished but dist\app.exe was not created.
  exit /b 1
)

echo.
echo [OK] Built: %CD%\dist\app.exe
endlocal
exit /b 0
