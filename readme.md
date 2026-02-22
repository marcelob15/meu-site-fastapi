# Criar o ambiente virtual
python -m venv .venv

# Ativar no PowerShell
# Se der erro de "script execution", rode: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1

uvicorn main:app --reload --port 9000