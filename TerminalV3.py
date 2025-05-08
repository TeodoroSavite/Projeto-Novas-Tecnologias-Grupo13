"""
Como usar:
────────────────────────────────────────────────────────────────────
1. Instale as dependências (no terminal do VSCode):

   py -m pip install requests beautifulsoup4

2. Salve este arquivo como, por exemplo: monitor_ministerios.py

3. Execute no terminal do VSCode:

   py monitor_ministerios.py

4. Digite o número do ministério que quer acompanhar (ex: 1) e tecle Enter.

O programa fará UMA única busca, exibirá as notícias encontradas e
depois retornará ao menu para você escolher outro ministério.

Para sair do programa, feche a janela do terminal ou pressione Ctrl+C
no menu principal.
────────────────────────────────────────────────────────────────────
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import sys

# ─── CONFIGURAÇÃO ───────────────────────────────────────────────────────────────

MINISTERIOS = {
    '1': ('Agricultura e pecuária', 'https://www.gov.br/pt-br/noticias/agricultura-e-pecuaria'),
    '2': ('Assistência Social',       'https://www.gov.br/pt-br/noticias/assistencia-social'),
    '3': ('Ciência e Tecnologia',     'https://www.gov.br/pt-br/noticias/ciencia-e-tecnologia'),
    '4': ('Comunicação',              'https://www.gov.br/pt-br/noticias/comunicacao'),
    '5': ('Cultura e Esporte',        'https://www.gov.br/pt-br/noticias/cultura-artes-historia-e-esportes'),
    '6': ('Economia e Gestão Pública','https://www.gov.br/pt-br/noticias/financas-impostos-e-gestao-publica'),
    '7': ('Educação e Pesquisa',      'https://www.gov.br/pt-br/noticias/educacao-e-pesquisa'),
    '8': ('Energia',                  'https://www.gov.br/pt-br/noticias/energia-minerais-e-combustiveis'),
    '9': ('Forças Armadas e Defesa',  'https://www.gov.br/pt-br/noticias/forcas-armadas'),
    '10':('Infraestrutura',           'https://www.gov.br/pt-br/noticias/transito-e-transportes'),
    '11':('Justiça e Segurança',      'https://www.gov.br/pt-br/noticias/justica-e-seguranca'),
    '12':('Meio Ambiente',            'https://www.gov.br/pt-br/noticias/meio-ambiente-e-clima'),
    '13':('Trabalho e Previdência',   'https://www.gov.br/pt-br/noticias/trabalho-e-previdencia'),
    '14':('Turismo',                  'https://www.gov.br/pt-br/noticias/viagens-e-turismo'),
}

INTERVALO = 0  # não usado aqui, pois fazemos apenas 1 busca por execução

# ─── FUNÇÕES ─────────────────────────────────────────────────────────────────────

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    clear_screen()
    print("=== Monitor de Notícias dos Ministérios ===\n")
    print("Escolha um ministério para acompanhar (digite apenas 1 número):\n")
    for chave, (nome, _) in MINISTERIOS.items():
        print(f"  {chave}. {nome}")
    escolha = input("\nSua escolha: ").strip()
    if escolha not in MINISTERIOS:
        print("\nOpção inválida. Tente novamente...")
        time.sleep(2)
        return exibir_menu()
    return escolha

def buscar_noticias(url):
    """Retorna lista de (titulo, link) ignorando <a> sem texto."""
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    artigos = soup.find_all('article')
    resultados = []
    for art in artigos:
        # procure o primeiro <a> que tenha texto
        encontrado = False
        for a in art.find_all('a'):
            titulo = a.get_text(strip=True)
            if titulo:
                link = a['href']
                if link.startswith('/'):
                    link = 'https://www.gov.br' + link
                resultados.append((titulo, link))
                encontrado = True
                break
        # se nenhum <a> com texto, pula este article
    return resultados

def format_link(titulo, link):
    return f"\033[1m\033]8;;{link}\033\\{titulo}\033]8;;\033\\\033[0m"

def monitorar(min_key):
    nome, url = MINISTERIOS[min_key]
    clear_screen()
    print(f"=== Notícias recentes em {nome}: ===")
    try:
        noticias = buscar_noticias(url)
    except Exception as e:
        print(f"[Erro ao buscar {nome}]: {e}")
        time.sleep(2)
        return

    if noticias:
        print()  # uma linha antes da 1ª notícia
        for i, (titulo, link) in enumerate(noticias, start=1):
            # exibe número, hífen, depois o link formatado
            print(f"{i} - {format_link(titulo, link)}")
            print()  # primeira linha em branco
            print()  # segunda linha em branco
    else:
        print("\nNenhuma notícia encontrada.\n")

    input("Pressione Enter para voltar ao menu...")


# ─── PROGRAMA PRINCIPAL ─────────────────────────────────────────────────────────

def main():
    while True:
        chave = exibir_menu()
        monitorar(chave)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("Programa encerrado. Até a próxima!")
        sys.exit(0)
    except Exception as e:
        print(f"Erro inesperado: {e}", file=sys.stderr)
        sys.exit(1)
