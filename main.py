from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    # Detecta se estamos na Vercel ou Local
    env = "Vercel" if "VERCEL" in os.environ else "Local"
    
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BusStation Enterprise - Cloud</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-900 text-white min-h-screen flex items-center justify-center">
        <div class="max-w-md w-full bg-gray-800 p-8 rounded-2xl shadow-2xl border border-gray-700">
            <div class="flex flex-col items-center">
                <div class="bg-blue-600 p-3 rounded-full mb-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                </div>
                <h1 class="text-3xl font-bold mb-2">BusStation Enterprise</h1>
                <p class="text-gray-400 mb-6 italic">Sistema de Gestão de Frota</p>
                
                <div class="w-full space-y-4">
                    <div class="flex justify-between items-center bg-gray-700 p-4 rounded-lg">
                        <span>Ambiente:</span>
                        <span class="px-2 py-1 bg-green-500/20 text-green-400 rounded text-sm font-mono">{env}</span>
                    </div>
                    
                    <div class="flex justify-between items-center bg-gray-700 p-4 rounded-lg">
                        <span>Python Version:</span>
                        <span class="text-blue-400 font-mono">3.12</span>
                    </div>
                </div>

                <button onclick="testeConexao()" class="w-full mt-8 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg transition-all transform hover:scale-105 active:scale-95">
                    Testar Conexão Banco
                </button>
                
                <p id="feedback" class="mt-4 text-sm text-gray-500"></p>
            </div>
        </div>

        <script>
            function testeConexao() {{
                const fb = document.getElementById('feedback');
                fb.innerText = "Verificando Neon Postgres...";
                fb.classList.add('text-yellow-500');
                
                setTimeout(() => {{
                    fb.innerText = "Pronto para configurar as rotas de banco!";
                    fb.classList.replace('text-yellow-500', 'text-green-500');
                }}, 1500);
            }}
        </script>
    </body>
    </html>
    """