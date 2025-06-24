@echo off
echo 📦 Installing dependencies for Windows...

:: Make sure python and pip are in PATH
where python >nul 2>&1 || (
echo ❌ Python is not in PATH.
pause
exit /b
)

:: Upgrade pip
python -m pip install --upgrade pip setuptools wheel

:: Install requirements
python -m pip install -r requirements.txt

echo ✅ All dependencies are installed on Windows.
pause