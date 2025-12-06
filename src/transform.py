
def fasta_parse(dados):
    registros = []
    sequencia_atual = ""
    cabecalho = ""
    nomes = []

    for linha in dados.split("\n"):
        if linha.startswith(">"):
            nome_orquidea = linha.split()[-9]
            nomes.append(nome_orquidea)
            if cabecalho:
                registros.append((cabecalho, sequencia_atual, nome_orquidea))
            cabecalho= linha
            sequencia_atual = ""
        else:
            sequencia_atual += linha.strip()
    
    if cabecalho:
        registros.append((cabecalho, sequencia_atual, nome_orquidea))

    return registros

def calcular_gc(seq):
    g = seq.count("G")
    c = seq.count("C")
    return round((g+c) / len(seq) * 100, 2)

def trasnformar_dados(dados):
    registros = fasta_parse(dados)
    results = []

    for cabecalho, sequencia, nome in registros:
        resultado = {
            "id": cabecalho,
            "Nome da Espécie": nome,
            "tamanho": len(sequencia),
            "Porcentagem de GC": calcular_gc(sequencia)
        }
        results.append(resultado)

    return results
