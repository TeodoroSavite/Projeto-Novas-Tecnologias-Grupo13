📡 Monitor de Notícias dos Ministérios (Brasil)
Um script em Python que permite monitorar as notícias recentes publicadas nos portais oficiais dos ministérios do governo brasileiro. As notícias são exibidas com links clicáveis diretamente no terminal.

🖥️ Pré-requisitos
Python 3.8+

Visual Studio Code (recomendado)

Conexão com a internet

🚀 Como instalar e rodar (passo a passo completo)
1. Instalar o Python
Acesse: https://www.python.org/downloads/windows/

Baixe e instale a versão mais recente do Python 3.x

Importante: Marque a opção "Add Python to PATH" antes de clicar em Install Now

2. Instalar o Visual Studio Code (VSCode)
Acesse: https://code.visualstudio.com/

Baixe e instale o VSCode normalmente.

3. Configurar o VSCode para Python
Abra o VSCode

Pressione Ctrl+Shift+X e instale a extensão chamada Python (Microsoft)

Opcional: também é recomendado instalar Pylance para uma experiência melhor.

4. Baixar e preparar o código
Crie uma nova pasta no seu computador (ex: monitor_ministerios)

Abra essa pasta no VSCode (vá em File → Open Folder)

Crie um novo arquivo chamado monitor_ministerios.py

Copie e cole todo o código do script nesse arquivo e salve (Ctrl+S)

5. Abrir o terminal integrado no VSCode
Pressione Ctrl+ (tecla acima do Tab) para abrir o terminal.

Confirme que o VSCode está usando o Python correto (canto inferior direito → "Python 3.x")

6. Instalar as dependências
No terminal integrado, digite:

bash
Copy
Edit
py -m pip install requests beautifulsoup4
7. Rodar o programa
Ainda no terminal, execute:

bash
Copy
Edit
py monitor_ministerios.py
✅ Como usar
Escolha o ministério digitando o número correspondente e pressione Enter.

As notícias mais recentes aparecerão com links clicáveis.

Para abrir uma notícia: segure Ctrl e clique no link com o botão esquerdo do mouse.

Pressione Enter para voltar ao menu e escolher outro ministério.

Para sair, pressione Ctrl+C no menu principal.

📰 Fontes monitoradas
O programa coleta notícias diretamente do portal oficial do Governo do Brasil:

https://www.gov.br/pt-br/noticias/

📚 Tecnologias usadas
Python 3

Requests

BeautifulSoup4

Terminal ANSI com links clicáveis (suportado no terminal integrado do VSCode)

⚠️ Avisos
Este projeto é educacional e não é afiliado com o Governo do Brasil.

As notícias são coletadas publicamente sem autenticação.

Testado no Windows usando VSCode + terminal integrado.

📄 Licença
Este projeto é de uso livre para fins educacionais e pessoais.
Créditos: desenvolvido por [Teodoro Martins, Tibor Hodos, Yohanna Araújo]
