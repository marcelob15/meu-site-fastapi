from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

app = FastAPI()

# Pega a URL do banco das variáveis de ambiente
DATABASE_URL = os.getenv("POSTGRES_URL")

# Configuração SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Acesso(Base):
    __tablename__ = "acessos"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    plataforma = Column(String)

@app.get("/", response_class=HTMLResponse)
async def home():
    # Salva um registro automático ao carregar a página
    db = SessionLocal()
    try:
        novo_acesso = Acesso(plataforma="Vercel" if "VERCEL" in os.environ else "Local")
        db.add(novo_acesso)
        db.commit()
    finally:
        db.close()

    return """
    <html>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px; background: #111; color: #fff;">
            <h1>BusStation + Neon Postgres</h1>
            <p style="color: #4ade80;">✅ Acesso registrado no banco com sucesso!</p>
            <a href="/" style="color: #3b82f6;">Atualizar página</a>
        </body>
    </html>
    """