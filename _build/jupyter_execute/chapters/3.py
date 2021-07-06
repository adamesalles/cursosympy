#!/usr/bin/env python
# coding: utf-8

# # Primeiros Passos com o Sympy
# 
# ## Instalação
# 
# Você possivelmente deve estar se perguntando como instalar o `Sympy`. Se você já utilizou algum outro módulo em Python, possivelmente imaginou em instalá-lo utilizando o `pip` (software que pedimos que garantisse sua sua instalação no capítulo 0).
# 
# Contudo, se você utiliza está utilizando notebooks com o Anaconda (nossa recomendação para esse módulo), o `Sympy` já está instalado, basta carregá-lo.
# 
# Caso esteja desenvolvendo em outro ambiente, uma forma de instalar é com o pip, por exemplo:
# 
# ```bash
# pip install sympy
# ```
# 
# ## Carregando o Módulo
# 
# Para utilizar os comandos do `Sympy` de forma nativa em nossos scripts, precisamos importá-lo globalmente. Para isso utilizamos as palavras-chave `import` e `from`. Isso não foi abordado no capítulo anterior devido a sua complexidade, mas essa é uma forma de importar módulos em Python.
# 
# Portanto, basta criar e executar a seguinte _chunk_:

# In[1]:


from sympy import *
init_printing(use_unicode=True, use_latex='mathjax') # Para imprimir LaTeX


# O `*` significa que estamos importando o módulo por completo.

# ## Trabalhando com expressões matemáticas
# 
# Como o `Sympy` tem como objetivo o cálculo simbólico, tudo é baseado a partir dos simbólos. Ou seja, as nossas querídas variáveis (como $x$, $y$, e $z$) sendo interpretadas com suas propriedades matemáticas. 
# 
# Portanto, para utilizá-las, precisamos criar seus símbolos. Por enquanto, vamos utilizar somente o $x$. Então, para o `x` do Python significar a variável $x$ fazemos:

# In[2]:


x = symbols('x')
x


# Note que nossa saída matemática será processada por um compilador $\LaTeX$ para facilitar a leitura.
# 
# No caso, você pode utilizar `x` como um número, e as expressões aparecerão normalmente (sem igualdade).

# In[3]:


x**2 - 4*x + 3


# Caso você queira a solução de uma expressão que seja igual a 0 (ou suas raízes, em outras palavras), em respeito a uma variável, você pode usar a função `solve()`. Ela recebe dois parâmetros obrigatórios, sua expressão e a variável que você quer a solução.

# In[4]:


solve(x**2 - 4*x + 3, x)


# In[5]:


solve(sqrt(x) - (x/2),x)


# Inclusive, caso queira uma resposta como costumamos escrever no papel, ou seja, em forma de conjunto e suas condições, podemos utilizar o `solveset()`. A maior diferença é que ele pode receber o conjunto numérico onde você quer trabalhar através do parâmetro `domain`. Na maioria das vezes podemos utilizar `domain=S.Reals` ou `domain=S.Complexes`.

# In[195]:


solveset(x**2 - 4*x  +20,x, domain=S.Reals)


# In[196]:


solveset(x**2 - 4*x  +20,x, domain=S.Complexes)


# In[209]:


solveset(tan(x), x, domain=S.Reals)


# Vamos criar uma variável para armazenar essa primeira expressão para mostrar outros exemplos

# In[6]:


expr = x**2 - 4*x + 3


# Podemos achar valores utilizando o método `subs()`. Novamente, devemos especficiar a variável.

# In[7]:


expr.subs(x,2) # Se y = expr, esse é o valor de y quando x = 2.


# In[8]:


expr.subs(x,1)


# Se tivermos uma expressão numérica não-inteira e quisermos achar a solução em um ponto flutuante (`float`), podemos usar o método `evalf()`.

# In[9]:


my_sqrt = sqrt(8)
my_sqrt


# In[10]:


my_sqrt.evalf()


# Como viu acima, possivelmente há uma função do `SymPy` que represente uma operação ou função matemática. Por exemplo, temos `sqrt()`, `log()`, `exp()`, `sin()` e etc. Quando sentir necessidade de utilizar uma dessa, tente antes de consultar a documentação. Caso não consiga "adivinhar", faça uma consulta que, com toda certeza, haverá uma função que te atenderá.

# Existem algumas funções que "fazem Álgebra" por si só. Veja alguns exemplos:

# In[11]:


# Simplifica
simplify((x**2 + x)/x) 


# In[12]:


# Fatora
factor(1-1/x)


# In[13]:


# Expande
expand((x**2 + 3*x)**3)


# In[14]:


# Agrupa potências de uma variável (que vai como segundo parâmetro)
collect(x**2 + 4*x - 2*x**2 + x -20 + x**3 + 2, x)


# In[15]:


# Separa fração em frações parciais
apart((x**2 + 8*x-18)/(x**3 + 3*x**2))


# Além desses principais, ainda há `trigsimp()` e `expand_trig()` que simplificam e expandem funções trigonométricas (a partir das identidades de adição de arco). E outras que fazem o mesmo para potências, logaritmos e outros tipos de funções. Nesse caso, acho que vale a pena dar uma olhada na documentação. Elas todas são bem parecidas.
# 
# Finalizando esse tópico inicial, temos como substituir uma função em termos de outra. Por exemplo:

# In[16]:


sin(x).rewrite(cos)


# In[17]:


(x**3).rewrite(exp)


# ### Equações
# 
# Ok, nós vimos como utilizar expressões. Mas, como tratamos equações? Como vimos no capítulo anterior `=` significa atribuição e `==` é uma operação booleana (ou seja, recebemos `True` ou `False`).
# 
# Para equações criamos uma classe `Eq()`. Não se preocupe com a nomenclatura, é só uma forma de criar um objeto do tipo `Eq`. Para criar esse objeto, passamos dois argumentos: cada lado da equação, respectivamente. Veja:

# In[18]:


eq = Eq(x**2, 2)
eq


# Podemos utilizar o mesmo método para encontrar suas raízes.

# In[19]:


solve(eq,x)


# ### Igualdade
# 
# Como verificar igualdade entre duas expressões? O `==` só servirá para expressões identicas (não somente em valor, mas também nos termos expressos). Para isso, utilizamos o método `equals()`. Veja: 

# In[20]:


expr_1 = sin(x)**2


# In[21]:


expr_2 = .5*(1 -cos(2*x))


# Como veremos abaixo, pelo `==` as expressões seriam diferentes.

# In[22]:


expr_1 == expr_2


# Vejamos pelo método `equals()`:

# In[23]:


expr_1.equals(expr_2)


# Podemos visualizar a igualdade da seguinte forma:

# In[24]:


Eq(expr_1,expr_2)


# ### Sistemas de Equações
# 
# Podemos, também utilizando `solve()` encontrar as soluções de um sistema de equações. Basta passar uma lista com as equações como parâmetro.

# In[210]:


y, z = symbols('y z') # Criando o y simbólico
Eqs = []
Eqs.append(Eq(3*x - 3*y, 20))
Eqs.append(Eq(-7*x + 9*y, -10))
solve(Eqs, x, y)


# Caso esteja tentando resolver um sistema linear (como o acima), é possível utilizar o `linsolve()`.

# In[176]:


linsolve(Eqs, x, y)


# In[215]:


Eqs = []
Eqs.append(Eq(3*x - 3*y + 2*z, 20))
Eqs.append(Eq(-7*x + 9*y -4*z, -10))
Eqs.append(Eq(-7*x + 9*y + 5*z, 40))
linsolve(Eqs, x, y,z)


# In[221]:


Eqs = []
Eqs.append(Eq(x**2 + y**2, 18)) #  Elipse de centro (0,0) e R^2 = 18
Eqs.append(Eq(x, y)) # Reta identidade
nonlinsolve(Eqs, x, y) # Sistema não-linear (solve também serve). No nosso caso, 2 pontos de intersecção.


# ## Exercícios
# 
# Utilizando o que aprendeu nesse capítulo, tente resolver os seguintes exercícios:
# 
# 1. Encontre as raízes de cada uma das expressões abaixo. Depois encontre um par $(x,y)$ para cada:
# 
# $$x^3 - 8x^2 + 4x + 3 $$
# 
# $$\sin(x) + 2\cos(x)$$
# 
# $$\log\left|\dfrac{x^2 - x}{2}\right|$$
# 
# $$e^{-x^3 + 5x^2 -x} -1$$
# 
# 2. Encontre as soluções das equações abaixo:
# 
# $$x^4 - 4x^3 + x^2 - 30 = -x^2 + x - 40$$
# 
# $$2^{x^2 -x} = 3^x$$
# 
# $$\log\left|x^3 - 2x^2 +x\right| = \log\left|x^2 + 6x\right|$$
# 
# 3. Verifique se as igualdades são verdadeiras:
# 
# $$\Gamma\left(\dfrac{3}{2}\right) = \dfrac{\sqrt{\pi}}{2}$$
# 
# $$\sin(2x^2) - \cos(x^2 +x) = \sin{\left(x \right)} \sin{\left(x^{2} \right)} + 2 \sin{\left(x^{2} \right)} \cos{\left(x^{2} \right)} - \cos{\left(x \right)} \cos{\left(x^{2} \right)}$$
# 
# $$(x^2 -3x)(2x^4 + x^3 - x)(-4x^2)= 8 x^{8} + 20 x^{7} + 12 x^{6} + 4 x^{5} - 12 x^{4}$$
# 
# 4. Encontre as soluções do sistema:
# 
# $$\begin{cases}4x - 3y + 2z = 60\\ (x - 10)^2 + y^2 + z^2 = 72\\ 2x + 9y +z = 20 \end{cases}$$
