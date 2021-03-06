#!/usr/bin/env python
# coding: utf-8

# # Conhecendo e Preparando o Ambiente
# 
# ## Introdução
# 
# Esse curso busca capacitar seus estudantes no tocante à biblioteca Sympy, do Python. Portanto, há a necessidade do conhecimento do próprio Python base. Com isso, o curso foi dividido em uma ordem lógica de aprendizagem para que o aluno consiga aprender continuamente, sem grandes "degraus" entre os assuntos. O capítulo 1 é uma introdução ao Python base, o que é suficiente para esse curso.
# 
# Neste capítulo, temos como objetivo fazer a instalação e configuração do nosso ambiente de desenvolvimento. Se você já é desenvolvedor Python, não acredito que seja necessária sua mudança ao ambiente que será indicado a esse curso. Mas, caso seja iniciante, recomendo que siga as instruções.
# 
# ## Escolhendo um Ambiente
# 
# Há duas opções para seguir esse curso: 
# 
# 1. Na forma de Notebooks
# 2. Na forma de Scripts
# 
# No curso, serão utilizado notebooks. Mais especificamente, Jupyter Notebooks, através do ambiente JupyterHub. Mas, não se preocupe, ambas as opções serão eficientes. Embora a utilização do Sympy seja regularmente associada ao desenvolvimento em Jupyter.
# 
# Na primeira opção, você só terá que instalar um pacote que virá com tudo incluso (IDE, Pacotes, etc.), e sua programação será mais parecida como um caderno. Onde você pode escrever, colocar imagens, matemática, e separar o código em blocos. Contudo, ele é mais pesado e menos flexível.
# 
# Na segunda opção, você terá um ambiente mais semelhante à programação tradicional. Linha após linha e comentários. Você terá que instalar o Python puro, versionar/atualizar seus módulos manualmente (o que é mais trabalhoso, mas dá mais autonomia) e utilizar um Editor de Código/IDE.
# 
# Caso não tenha entendido o que fora explicado acima, acredito que, nesse momento inicial, a primeira opção é a melhor para você. Contudo, ela não te ajudará a migrar para outra linguagem de programação no futuro, caso queira ou seja necessário. (Isso não é um problema, ao meu ver).
# 
# ## Instalando o Ambiente (1ª Opção)
# 
# ### Windows
# 
# No Windows, a instalação é bem simples, utilizaremos o Anaconda. Para isso, baixe o [instalador do Anaconda](https://www.anaconda.com/download/#windows). 
# 
# Prossiga a instalação normalmente. Contudo, preste atenção às duas caixas de marcação (checkboxes) que perguntam sobre adicionar o Anaconda ao PATH e torná-lo padrão. Ambas as opções devem estar marcadas. 
# 
# Se ele oferecer a instalação de algum outro IDE (como o PyCharm), você pode negar.
# 
# ### Linux
# 
# A instalação no Linux é um pouco mais complicada. Mas, se você utiliza Linux, possivelmente consegue instalar com certa facilidade.
# 
# Verifique as dependências da sua distribuição nesse link: <https://docs.anaconda.com/anaconda/install/linux/>
# 
# E depois siga a instalação com o [instalador para Linux](https://www.anaconda.com/download/#linux). Ele é um instalador em Bash, então recomendo que utilize os comandos prescritos no site do Anaconda.
# 
# ## Instalando o Ambiente (2ª Opção)
# 
# Como dito na seção anterior, para essa opção temos que instalar 2 programas, além dos pacotes separadamente.
# 
# ### Windows
# 
# No Windows, você terá que baixar e instalar o Python que está disponível nesse link: <https://www.python.org/downloads/>
# 
# A instalação é bem simples, você só deve se certificar que ele será adicionado ao PATH e que o `pip` será instalado. (São duas caixinhas de marcar que devem aparecer)
# 
# Para testar se a instalação deu certo, abra um prompt de comando (basta inserir ou cmd ou powershell no menu de pesquisa) e digite:
# 
# ```bash
# py --version
# ```
# 
# Deve aparecer a versão do Python que você instalou. Caso isso não ocorra, repita o procedimento e veja se fez tudo corretamente.
# 
# Também confirme se o pip foi instalado corretamente:
# 
# ```bash
# pip --version
# ```
# 
# Após isso, você deve escolher um editor. A minha recomendação é o [Visual Studio Code](https://code.visualstudio.com/). 
# 
# Mas você pode utilizar outros como o [Atom](https://atom.io/) ou [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/).
# 
# A instalação de todos é bem simples. Ao abri-los, certifique-se se é necessário instalar uma extensão para suporte ao Python. Caso for, instale-a.
# 
# ### Linux
# 
# No Linux, a imensa maioria das distribuições já vêm com o Python instalado e disponível. A única diferença é que algumas adotam o nome `python3` e outras somente `python`.
# 
# Para isso, teste no terminal:
# 
# ```bash
# python --version
# python3 --version
# ```
# 
# E comece a usar o que tem a versão mais atual.
# 
# Também certifique-se se você tem o `pip` instalado
# 
# ```bash
# pip --version
# pip3 --version
# ```
# 
# Caso não tenha, veja como instalá-lo em sua distribuição.
# 
# Assim como no Windows, você deve instalar um editor. As minhas recomendações são as mesmas para o Windows. Ou seja, primeiramente o [Visual Studio Code](https://code.visualstudio.com/). E depois ou o [Atom](https://atom.io/) ou o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/).
# 
# Todos têm versão para Linux e a instalação deve ser até mais simples que para windows. No caso do Visual Studio Code, recomendo que utilize a versão flatpak ou snap.
# 
# ## Como acompanhar as explicações do curso
# 
# O nosso curso será baseado em Jupyter Notebooks, uma forma de programar em blocos. Esses blocos podem ser tanto de código como de texto.
# 
# No caso, a primeira opção de ambiente lhe entregará um ambiente muito parecido com o que eu utilizei para escrever os meus Notebooks. Para a segunda, acredito que será mais difícil. Principalmente, pela ausência de alguns pacotes e softwares que vêm com o Anaconda. Mas, decidi incluí-la, pois há pessoas que precisam somente de uma consulta rápida, e possivelmente já têm seu ambiente de desenvolvimento, sendo em Anaconda ou não.
# 
# Então, para a primeira opção, você deverá abrir o "Anaconda Navigator". Esse software servirá como gerenciador de pacotes e dos serviços. 
# 
# Como dito anteriormente, utilizaremos Jupyter Notebooks. Então basta clicar em "Launch" no card do Jupyter Notebook.
# 
# Ele abrirá um navegador de arquivos no navegador, semelhante a um site. Basta escolher uma pasta onde gostaria de criar seus notebooks, e criá-los a partir do botão "New" e então escolha o _Python 3_.
# 
# O curso não tem como foco específico ensinar o uso desse ambiente, uma vez que ele é bem simples. Basicamente, você deverá criar blocos (que costumamos chamar de _chunks_) de forma a organizar o entendimento e a saída do seu código. Ao escolher a opção "Code" para seu bloco, você deverá escrever códigos Python nele. No caso de "Markdown", você deverá escrever texto de acordo com a sintaxe da linguagem de marcação Markdown. 
# 
# Essa sintaxe é bem simples, dê uma olhada nessa "tabela de cola": <https://github.com/luong-komorebi/Markdown-Tutorial/blob/master/README_pt-BR.md>
# 
# Para qualquer tipo de bloco, basta segurar a tecla Ctrl e apertar Enter para compilá-lo.
# 

# ## Exercícios
# 
# 1. Crie um chunk de markdown e escreva um título com o texto "Olá mundo em Python".
# 2. Abaixo desse chunk, crie outro com o código `print('Olá mundo')`.

# ## Próximos passos
# 
# Embora esse capítulo não tenha tido um bloco sequer de código, acredito que agora estão preparados para aprender os básicos de Python
