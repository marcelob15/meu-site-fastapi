# Criar o ambiente virtual
python -m venv .venv

# Ativar no PowerShell
# Se der erro de "script execution", rode: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1

uvicorn main:app --reload --port 9000


pip freeze > requirements.txt





1. Criar a tabela no Neon
Antes de rodar o código, vá ao console do Neon, clique em SQL Editor e execute:

SQL
CREATE TABLE IF NOT EXISTS acessos (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    plataforma TEXT
);


SELECT * FROM acessos;