from src.extract import extract_data
from src.transform import trasnformar_dados
import os
import json

if __name__ == "__main__":
    dados = extract_data()
    resultados = trasnformar_dados(dados)

    os.makedirs("data", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    caminho_arquivo = "data/processed/resultados.json"

    with open(caminho_arquivo, "w", encoding="utf-8") as file:
        json.dump(resultados, file, indent=4, ensure_ascii=False)

    print("✅ Arquivo salvo em:", caminho_arquivo)