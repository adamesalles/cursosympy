#!/usr/bin/env python
# coding: utf-8

# # Aplicações em Cálculo Diferencial e Integral
# 
# De modo geral, o principal objetivo do curso é garantir que seus alunos estejam proeficientes no uso de `SymPy` no Cálculo. Na minha opinião, esse é o capítulo mais importante do curso. Dê seu máximo para absorver o conteúdo aqui apresentado.
# 
# Antes de comerçarmos, certifique-se que fez as devidas importações e atribuições:

# In[1]:


from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True, use_latex='mathjax')


# ## Intervalos
# 
# Nós sabemos que o Cálculo é, genericamente, o estudo das mudanças. E nós costumamos definir intervalos para trabalhar com nossas funções e expressões. É bem simples de criá-los e utilizá-los no `SymPy`.
# 
# Para criar um intervalo, criamos um objeto a partir da classe `Interval` e/ou um método seu para definir se está aberto em algum dos lados. Veja os exemplos:

# In[2]:


# Intervalo Fechado
Interval(0,10)


# In[3]:


# Intervalo Aberto
Interval.open(-10, 20)


# In[4]:


# Intervalo Aberto em um dos lados
Interval.Ropen(10,30) # R - Direita


# In[5]:


Interval.Lopen(10,30) # L - Direita


# In[6]:


Interval(0,oo) # oo representa o infinito em sympy. Note que onde oo estiver será aberto.


# ## Análises de Domínio/Intervalo
# 
# Existem diversas funções embutidas no `SymPy` para avaliar o comportamento das funções/expressões ao longo de seu domínio ou de um intervalo específico. Normalmente elas retornarão um booleano.
# 
# ### Verificar se é crescente ou decrescente.

# In[7]:


## x² em seu domínio não é crescente
is_increasing(x**2)


# In[8]:


## x² em (0, oo) é crescente
is_increasing(x**2, Interval.open(0, oo))


# In[9]:


## O contrário vale para decreasing
is_decreasing(x**2, Interval.open(-oo, 0))


# Podemos verificar também se ela é estritamente crescente ou decrescente, ou seja, se ela é injetiva. 

# In[10]:


## x³ é crescente em todo seu domínio. (d/dx = 3x² >= 0)
is_increasing(x**3)


# In[11]:


## x³ não é estritamente crescente em seu domínio (3*0² = 0)
is_strictly_increasing(x**3)


# In[12]:


## 1/(e^x) é estritamente decrescente em seu domínio
is_strictly_decreasing(1/(exp(x)))


# Podemos também verificar se ela é monótona com `is_monotonic()`. Para finalizar, podemos verificar se há pontos (e quais são) com singularidades. Ou seja, que requerem certa atenção. Normalmente, são pontos que não têm limite. 

# In[13]:


singularities(1/x,x)


# ## Limites
# 
# Assim como veremos posteriormente nas derivadas e nas integrais, há duas formas de criar e calcular limites no `SymPy`. A primeria forma é através da classe `Limit`, que criará um limite e não calculará seu valor. Ou seja, utilize ela para armazenar a expressão do limite. Caso queira somente calcular o limite. Utilizamos a função `limit()`.

# In[14]:


Limit(sin(x)/x, x, 0, '+') ## sin(x)/x, x -> 0+


# In[15]:


Limit(1/x, x, 0, '-') ## sin(x)/x, x -> 0-


# In[16]:


limit(sin(x)/x, x, 0, '+')


# In[17]:


limit(1/x, x, 0) # '+' por padrão


# In[18]:


limit(1/x, x, 0, '-')


# In[19]:


limit(1/x, x, 0, '+-') # Dois lados


# In[20]:


my_sin = Limit(sin(x)/x, x, 0, '+')
my_sin.doit() # Método doit() calcula uma expressão.


# ## Derivadas
# 
# Assim com os limites, podemos criar a derivada (sem calculá-la) através da classe `Derivative()`. E calcular diretamente através da `diff()`.

# In[21]:


Derivative(exp(2*x**3),x)


# In[22]:


diff(sin(x**2),x)


# In[23]:


diff(sin(x**2),x, x) ## Calcular a segunda derivada


# In[24]:


diff(sin(x**2),x, x, x) ## Calcular a terceira derivada


# In[25]:


diff(sin(x**2),x, 3) ## Calcular a terceira derivada de outra forma


# In[26]:


diff(sin(x**2),x, 10) ## Calcular a décima derivada


# In[27]:


my_deriv = Derivative(exp(2*x**3),x)
my_deriv.doit()


# In[28]:


## Podemos, com o método diff()
expr = exp(2*x**3)
expr.diff(x)


# In[29]:


expr.diff(x,3) # Terceira derivada


# ## Integrais
# 
# Assim como os Limites e as Derivadas que vimos acima, podemos criar uma Integral através da classe `Integral()` caso queiramos ter somente a expressão, e caso queiramos o resultado de uma Integral, basta utilizar a função `integrate()`.
# 
# O `Sympy` não acresce a constante de integração nas Integrais Indefinidas, então é importante se lembrar delaa quando for resolver algum exercício.

# In[30]:


Integral(1/x, x)


# In[31]:


Integral(1/x, (x, 1, 10)) # Note que passamos (simbolo, inf, sup)


# In[32]:


integrate(1/x, (x,1,10))


# In[33]:


my_integral = Integral(1/x + 1/y, (x, 1, 10), (y, 1, 10)) # Integral dupla, duas variáveis.
my_integral


# In[34]:


my_integral.doit()


# In[35]:


Integral(exp(x**2 - 10), x,x) # Integral dupla indefinida, mesma variável


# ## Outras funções
# 
# ### Séries
# 
# Você pode utilizar o método `series()` em uma expressão para fazer sua expansão em série.

# In[36]:


asin(x).series(x,0, 10) # (x, x_0, n)


# ### Equações Diferenciais
# 
# Ao criar uma função simbólica, você pode utilizar derivadas e a função `dsolve()` para encontrar a solução de uma expressão e ou equação diferencial. Nesse caso, o `SymPy` insere as constantes quando necessário.

# In[37]:


f = Function('f')
my_deq = Eq(Derivative(f(x),x,2),f(x))
my_deq


# In[38]:


dsolve(my_deq)


# ## Exercícios
# 
# Como nos últimos capítulos, resolva os seguintes exercícios com o que aprendeu ao longo do curso.
# 
# 1. Para cada uma das funções abaixo, encontre:
# 
# a) O domínio da função;
# 
# b) As assíntotas horizontais e verticais, caso existam;
# 
# c) Sua derivada, os intervalos de crescimento e decrescimento de f,os pontos de máximo e mínimo, caso existam; 
# 
# d) Os intervalos onde o gráfico da f é côncavo para cima e onde é côncavo para baixo.
# 
# $$f(x) = \dfrac{x^3}{x + 4}$$
# 
# $$g(x) = \dfrac{x^3 - 4x^2 + 5}{x^2 - x}$$
# 
# $$h(x) = x^2 - 4x + \dfrac{x}{x-10}$$
# 
# 2. Calcule:
# 
# $$\int x^3 - 2x^2 + 3x + 10 \,\ dx$$
# 
# $$\int x^3\cdot\sin(2x) \,\ dx$$
# 
# $$\int_0^{10} \tan^3(x)\sec^3(x) \,\ dx $$
# 
# $$\int_1^{\infty} -\dfrac{1}{x^2} \,\ dx $$
# 
# 3. Qual a menor distância vertical entre as funções $f(x) = 32x^2$ e $g(x) = -\dfrac{8}{x^2}$?
