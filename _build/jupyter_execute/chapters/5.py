#!/usr/bin/env python
# coding: utf-8

# # Criando Gráficos
# 
# O uso de gráficos na matemática, principalmente no Cálculo e na Geometria Analítica, é de extrema importância. Embora esse não seja o foco do `SymPy`, é possível criar os chamados _plots_ com certa facilidade. Inclusive, como é utilizado o `matplotlib` para criar os gráficos, há uma grande margem para alterações. Isso permite gráficos quase totalmente customizáveis.
# 
# Os tipos de plots abordados nesse capítulos serão os criados pelas funções:
# 
# - plot()
# - plot_implicit()
# - plot3d()
# 
# O seu uso é facilitado mais ainda pelo ambiente Jupyter, e podemos trabalhar com eles de forma semelhante ao que fora abordado no último capítulo. Ou seja, podemos criar um objeto para trabalharmos com ele, e depois ver o resultado. Ou, podemos simplesmente criar um plot.
# 
# Antes de começarmos, vamos a importação e as definições essenciais:

# In[1]:


from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True, use_latex='mathjax')


# ## Plot 2D
# 
# As duas primeiras funções que trabalharemos criam plots em 2D. Para fazer um plot de uma função, basta utilizar a função `plot()`. Confira abaixo:

# In[2]:


plot(x**3)


# Podemos, inclusive, fazer vários plots unidos.

# In[3]:


plot(x**3, x**2)


# Obviamente, o gráfico acima está longe de ser o melhor possível. Mas com apenas uma função fizemos algo relevante. Mas, se armazenarmos, note o que podemos fazer.

# In[4]:


my_plot = plot(x**3, x**2, show=False) # show=False para não plotar.
my_plot.show() # .show() para exibir


# Por enquanto, nada mudou. Mas podemos ir trabalhando em seus atributos assim.

# In[5]:


my_plot[1].line_color = 'red' # x²
my_plot.show()


# Estamos melhorando. Veja que `my_plot` armazena as funções em sequência. Trabalhamos em $x^2$ individualmente quando usamos `my_plot[1]`.

# In[6]:


my_plot.legend = True # Legenda
my_plot.xlim = (-10,10) # Esse é o máximo por padrão, veremos como alterar isso mais tarde
my_plot.ylim = (-100,100)
my_plot.size = (8,6) # Tamanho da figura
my_plot.show()


# Acho que conseguimos um bom resultado. Contudo, você concorda que é um pouco cansativo acessar cada um desses valores e ir alterando, certo? E, se não definíssemos os limites em $x$ para $[-10,10]$, você veria que a função não continuaria. Isso ocorre pois não definimos o alcance de nosso plot ao criá-lo.
# 
# Aliado a isso, é possível criar dois plots diferentes e uní-los com o método `.extend()`.
# 
# Com o que aprendemos podemos fazer, com um único comando, um bom plot de uma única função. Caso queiramos mais de uma (como fizemos acima), basta alterar as cores de suas linhas.
# 
# Caso você conheça `matplotlib`, é possível utilizar todos os parâmetros para anotações e etc. Não abordarei isso aqui pois acredito que foge do nosso objetivo, mas é algo interessante.
# 

# In[7]:


p1 = plot(exp(x), log(x),x, (x, -2, 10), ylim = (-2,10), legend = True, size = (6,6), show=False)
p1[1].line_color = 'red'
p1[2].line_color = 'green'
p1.show()

