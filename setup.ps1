# Allow script execution for this session only
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

# Define virtual environment path
$venvPath = ".\venv"

# Remove existing virtual environment (if any)
if (Test-Path $venvPath) {
    Write-Host "Removing existing virtual environment..."
    Remove-Item -Recurse -Force $venvPath
}

# Create a new virtual environment
Write-Host "Creating a new virtual environment..."
python -m venv venv

# Activate the virtual environment
Write-Host "Activating the virtual environment..."
& .\venv\Scripts\Activate.ps1

# Install dependencies
if (Test-Path ".\requirements.txt") {
    Write-Host "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "requirements.txt not found. Skipping package installation."
}

Write-Host "`n✅ Environment is ready. You can start working."

# Launch the FastAPI app in a new terminal window
Write-Host "`n🚀 Launching FastAPI at http://127.0.0.1:8000 ..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd `"$PWD`"; .\venv\Scripts\Activate.ps1; uvicorn app.main:app --reload"
