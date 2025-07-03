# ---------------------------------------------------------------------------------#
# Extrair caracteries do arquivo exemplo
def extrair_caracteres_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            caracteres_ascii = [ord(c) for c in conteudo]  # Extrai os caracteres ASCII
        return caracteres_ascii
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    
# ---------------------------------------------------------------------------------#
# Filtro para caracteries
def filtrar_caracteres(caminho_arquivo, caracteres_indesejados):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            # Filtrando caracteres indesejados
            conteudo_filtrado = ''.join([c for c in conteudo if ord(c) not in caracteres_indesejados])
        return conteudo_filtrado
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return ""
    
# ---------------------------------------------------------------------------------#
# Listagem numerada

def listar_com_numeros(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            linhas_numeradas = [f"{i+1}: {linha.strip()}" for i, linha in enumerate(linhas)]
        return linhas_numeradas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []

from collections import defaultdict

# ---------------------------------------------------------------------------------#
# Extração e listagem de palavras por linha com referência de linha
def extrair_palavras_e_referencias(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

            tabela_referencias = defaultdict(set)

            for numero_linha, linha in enumerate(linhas, 1):
                palavras = linha.split()
                for palavra in palavras:
                    tabela_referencias[palavra.lower()].add(numero_linha)

            # Ordenando a tabela de referências
            tabela_ordenada = sorted(tabela_referencias.items())

        return tabela_ordenada
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []



if __name__ == "__main__":
    arquivo = "exemplo.txt"

    # 1) Extrair caracteres ASCII
    caracteres_ascii = extrair_caracteres_arquivo(arquivo)
    print("Caracteres ASCII extraídos:", caracteres_ascii)

    # 2) Filtrar caracteres indesejados
    caracteres_indesejados = [ord(c) for c in " \t\n\r"]  # Espaços, tabulações e novas linhas
    conteudo_filtrado = filtrar_caracteres(arquivo, caracteres_indesejados)
    print("Conteúdo filtrado:", conteudo_filtrado)

    # 3) Listagem numerada
    linhas_numeradas = listar_com_numeros(arquivo)
    print("Linhas numeradas:")
    for linha in linhas_numeradas:
        print(linha)

    # 4) Referências cruzadas
    tabela_referencias = extrair_palavras_e_referencias(arquivo)
    print("Tabela de referências cruzadas:")
    for palavra, linhas in tabela_referencias:
        print(f"{palavra}: {', '.join(map(str, sorted(linhas)))}")