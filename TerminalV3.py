"""
Como usar:
────────────────────────────────────────────────────────────────────
1. Instalar o Python:
   a) Abra o navegador e acesse https://www.python.org/downloads/windows/  
   b) Baixe o instalador do Python 3.x (ex: “Python 3.11.x”).  
   c) Durante a instalação, marque a caixinha “Add Python to PATH” e clique em “Install Now”.

2. Configurar o VSCode para Python:
   a) Abra o VSCode.  
   b) Vá em Extensions (ícone de quadrado na barra esquerda) ou pressione Ctrl+Shift+X.  
   c) Pesquise por “Python” (Microsoft) e clique em “Install”. 

3. Abrir o terminal integrado:
   a) Com o VSCode aberto, pressione Ctrl + ' (tecla acima do Tab) para abrir o terminal na parte inferior.  
   b) Garanta que, no canto inferior direito, o VSCode está usando o intérprete Python que você instalou.  
      - Clique onde aparece “Python 3.x.x” e selecione o intérprete correto se houver mais de um.

4. Criar e preparar o arquivo do programa:
   a) No VSCode, vá em File → New File.  
   b) Cole todo o código do monitoramento (monitor_ministerios.py).  
   c) Salve (Ctrl+S) com o nome **monitor_ministerios.py** em uma pasta de sua escolha.

5. Instalar dependências Python:
   No terminal integrado(aquele que você abriu usando ctrl + ') certifique‑se que está na pasta onde salvou o arquivo do 
   programa (monitor_ministérios.py) e escreva a linha abaixo, depois pressione enter:
   py -m pip install requests beautifulsoup4

6. Depois disso Basta "Rodar" o programa:
   a) Aperte no botão de "Play" no canto superior direito do VSCode ou
   b) Esreva essa linha no terminal  py monitor_ministerios.py e depois aperte enter.

7. Usando o programa:
- Digite o número do ministério que deseja (ex: 1) e tecle Enter.  
- Para abrir uma notícia no navegador, segure Ctrl e clique sobre o link. 
- O link abrirá em seu navegador. 
- Após visualizar a noticia, volte para o VSCode e pressione Enter no terminal para voltar ao menu e escolher outro ministério.

obs:
O programa fará UMA única busca e exibirá as notícias encontradas.

8. Para sair do programa, feche a janela do terminal ou pressione Ctrl+C
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
    print("Segure a tecla ctrl e clique com o botão esquerdo do mouse para poder abrir a noticia em seu navegador\n")
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
