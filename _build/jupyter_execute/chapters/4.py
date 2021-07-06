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


my_sin = Limit(sin(x)/x, x, 0, '+')
my_sin.doit() # Método doit() calcula uma expressão.


# ## Derivadas
# 
# Assim com os limites, podemos criar a derivada (sem calculá-la) através da classe `Derivative()`. E calcular diretamente através da `diff()`.

# In[20]:


Derivative(exp(2*x**3),x)


# In[21]:


diff(sin(x**2),x)


# In[22]:


diff(sin(x**2),x, x) ## Calcular a segunda derivada


# In[23]:


diff(sin(x**2),x, x, x) ## Calcular a terceira derivada


# In[24]:


diff(sin(x**2),x, 3) ## Calcular a terceira derivada de outra forma


# In[25]:


diff(sin(x**2),x, 10) ## Calcular a décima derivada


# In[26]:


my_deriv = Derivative(exp(2*x**3),x)
my_deriv.doit()


# In[27]:


## Podemos, com o método diff()
expr = exp(2*x**3)
expr.diff(x)


# In[28]:


expr.diff(x,3) # Terceira derivada

