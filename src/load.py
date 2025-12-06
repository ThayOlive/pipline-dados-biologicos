import json
import matplotlib.pyplot as plt
import os

os.makedirs("data/plots", exist_ok=True)

#construir visualização dos dados em fasta
with open("data/processed/resultados.json", "r") as file:
    dados = json.load(file)

ids = [d["id"][:30] for d in dados]  # encurta o nome
tamanhos = [d["tamanho"] for d in dados]
nomes = [d["Nome da Espécie"] for d in dados]
gc = [d["Porcentagem de GC"] for d in dados]


plt.figure(figsize=(10, 6))
plt.bar(nomes, tamanhos)
plt.xticks(rotation=90)
plt.title("Tamanho das Sequências de DNA")
plt.tight_layout()
plt.savefig("data/plots/tamanho_sequencias.png")
plt.close()


plt.figure(figsize=(10, 6))
plt.plot(nomes, gc, marker="o")
plt.xticks(rotation=90)
plt.title("Teor de GC (%) por sequência")
plt.tight_layout()
plt.savefig("data/plots/procentagem_gc.png")
plt.close()