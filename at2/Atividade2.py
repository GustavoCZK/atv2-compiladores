import os
from collections import defaultdict

# Caminho completo do arquivo
caminho = "/Users/402497/Desktop/at2/exemplo.txt"

# ---------------------------------------------------------------------------------#
# Extrair caracteres ASCII do arquivo
def extrair_caracteres_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            caracteres_ascii = [ord(c) for c in conteudo]  # Extrai os caracteres ASCII
        return caracteres_ascii
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return []

# ---------------------------------------------------------------------------------#
# Filtro para caracteres indesejados
def filtrar_caracteres(caminho, caracteres_indesejados):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            # Filtrando caracteres indesejados
            conteudo_filtrado = ''.join([c for c in conteudo if ord(c) not in caracteres_indesejados])
        return conteudo_filtrado
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return ""

# ---------------------------------------------------------------------------------#
# Listagem numerada
def listar_com_numeros(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            linhas_numeradas = [f"{i+1}: {linha.strip()}" for i, linha in enumerate(linhas)]
        return linhas_numeradas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return []

# ---------------------------------------------------------------------------------#
# Extração e listagem de palavras por linha com referência de linha
def extrair_palavras_e_referencias(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
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
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return []

# Função principal para rodar todas as partes
if __name__ == "__main__":
    if not os.path.exists(caminho):  # Verifica se o arquivo existe
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
    else:
        # 1) Extrair caracteres ASCII
        caracteres_ascii = extrair_caracteres_arquivo(caminho)
        print("Caracteres ASCII extraídos:")
        print(caracteres_ascii)

        # 2) Filtrar caracteres indesejados
        caracteres_indesejados = [ord(c) for c in " \t\n\r"]  # Espaços, tabulações e novas linhas
        conteudo_filtrado = filtrar_caracteres(caminho, caracteres_indesejados)
        print("\nConteúdo filtrado (sem espaços, tabulações e novas linhas):")
        print(conteudo_filtrado)

        # 3) Listagem numerada
        linhas_numeradas = listar_com_numeros(caminho)
        print("\nLinhas numeradas:")
        for linha in linhas_numeradas:
            print(linha)

        # 4) Referências cruzadas
        tabela_referencias = extrair_palavras_e_referencias(caminho)
        print("\nTabela de referências cruzadas (palavras e linhas):")
        for palavra, linhas in tabela_referencias:
            print(f"{palavra}: {', '.join(map(str, sorted(linhas)))}")
