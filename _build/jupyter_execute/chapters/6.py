#!/usr/bin/env python
# coding: utf-8

# # Extras
# 
# Como a principal intenção do curso é prepará-los para o uso de `SymPy` nas disciplinas que envolvem Cálculo, ao finalizar o capítulo anterior você deve estar pronto para resolver seus problemas utilizando esse módulo. Contudo, eu acredito que há muito a se falar sobre esse módulo. E, portanto, esse capítulo fará uma abordagem rápida sobre algumas coisas que são possíveis com ele.
# 
# ## Geometria
# 
# Isso mesmo, nós podemos resolver problemas de Geometria tanto de forma simbólica, como de forma numérica. A ideia principal não é ficar criando plots com o sistema completo, mas sim trabalhar matemáticamente (indo para o lado da Geometria Analítica). 
# 
# Antes de começarmos essa seção e as próximas, faremos as devidas importações e definições:

# In[1]:


from sympy import *
from sympy.geometry import * # Importante garantir que foi importado corretamente
x, y, z = symbols('x y z')
init_printing(use_unicode=True, use_latex='mathjax')


# ### 2D
# 
# Começando pela geometria em 2D, podemos seguir o processo de criar os pontos, as linhas (a partir dos pontos) e as formas 2D a partir dos segmentos. É bem simples e intuitivo, veja:

# In[2]:


O = Point(0,0)
A = Point(1,2)
B = Point(3,-4)
C = Point(-2, 3)


# Você pode fazer as operações padrões entre pontos normalmente. 

# In[3]:


B - A ## AB


# Contudo, o indicado é utilizar as classes, que já terão suas propriedades a fácil acesso.

# In[4]:


Segment(A,B) ## AB Simbólicamente


# In[5]:


AC = Segment(A,C)
AC.slope ## inclinação


# In[6]:


AC.length ## comprimento


# In[7]:


AC.midpoint ## ponto médio


# In[8]:


AC.contains(A) ## Contém A?


# In[9]:


AC.distance(B) ## Menor distância ao ponto B


# Nós podemos criar linhas também

# In[10]:


Line(A,B)


# In[11]:


l1 = Line(A,B)
l1.equation() ## Equação da reta = 0


# In[12]:


l1.coefficients ## Coeficientes da reta


# Podemos criar uma reta ao dar um ponto inicial e uma inclinação, lembrando que: $y - y_0 = m(x-x_0)$

# In[13]:


l2 = Line(C, slope = 3)
l2.equation()


# In[14]:


l3 = l2.perpendicular_line(A) ## Retorna uma reta perpendicular que passa pelo ponto dado
l3.equation()


# In[15]:


l3.slope # -m^-1


# E nós podemos ver a intersecção entre duas entidades geométricas.

# In[16]:


intersection(l2,l3)


# In[17]:


intersection(l1, l3) # Ponto A


# Para plotar, de modo geral, fazemos o uso do que aprendemos no último capítulo, a função `plot_implicit`.

# In[18]:


plot_implicit(l1.equation()) 


# Podemos criar figuras geométricas e encontrar suas áreas e verficiar intersecções. Veja os exemplos:

# In[19]:


trig = Triangle(A,B,C) # Cria um Triângulo
trig


# In[20]:


trig.area ## Não utiliza valores absolutos


# In[21]:


abs(trig.area) ## Correto


# In[22]:


trig.perimeter ## Perímetro


# In[23]:


trig.orthocenter ## Centro Ortogonal


# In[24]:


trig.circumcenter ## Circuncentro


# In[25]:


trig.altitudes ## Alturas


# In[26]:


trig.incircle ## Círculo interno


# In[27]:


trig.incircle.equation()


# In[28]:


trig.bisectors() ## Bissetrizes


# In[29]:


trig.bisectors()[A] ## Bissetriz que passa no ponto A


# In[30]:


trig.is_right() ## É triângulo retângulo?


# In[31]:


trig.is_scalene() ## É triângulo escaleno?


# In[32]:


circ = Circle(A, 3) ## Centro e Raio
circ


# In[33]:


circ.equation()


# In[34]:


circ.circumference


# In[35]:


circ.area


# In[36]:


intersection(trig,circ)


# In[37]:


elips = Ellipse(B, 3, 2) ## Centro, Raio Horizontal, Raio Vertical
elips


# In[38]:


elips.equation()


# In[39]:


elips.circumference ## Não há formulas


# In[40]:


elips.circumference.evalf() ## Valor numérico


# In[41]:


elips.area


# In[42]:


elips.eccentricity


# In[43]:


elips.foci ## Focos


# In[44]:


elips.focus_distance ## Distância Focal


# In[45]:


D = Point(0,10)
quad = Polygon(A,B,C,D) ## Criando Polígono de N vértices
quad


# In[46]:


abs(quad.area)


# In[47]:


quad.angles


# In[48]:


quad.angles[A] ## No ponto A


# In[49]:


from sympy.physics.units import degree ## Importação das unidades
(quad.angles[A]/degree.scale_factor).evalf() ## Transforma em Graus


# In[50]:


reg = RegularPolygon(A,1,4) # Centro, Raio, Qtd. Lados
reg


# In[51]:


reg.angles # Retângulo


# In[52]:


reg.vertices # Vértices


# Para finalizar com a Geometria, é importante relembrar que é possível fazer tudo isso com valores simbólicos. Por exemplo, um quadrado em função de um lado $x$:

# In[53]:


sim_quad = Polygon(Point(x/2, x/2), Point(-x/2, x/2),Point(-x/2, -x/2),Point(x/2, -x/2))
sim_quad


# In[54]:


sim_quad.area


# ### 3D
# 
# Para a terceira dimensão, podemos utilizar os Pontos com três coordenadas para gerar nossas formas.

# In[55]:


M = Point(1, 2, 3)
N = Point(-2, 3, 4)
P = Point(5, -8, 10)
Line(M,N)


# In[56]:


Line(M,N).equation()


# In[57]:


Plane(M,N,P) # Plano


# In[58]:


Plane(M,N,P).equation()


# ## Reações em Vigas (Mecânica)
# 
# Nós podemos analisar as tensões em vigas utilizando o `sympy.physics.continuum_mechanics`. Caso você procure aplicar carregamento em uma viga e então avaliar as reações e seus gráficos, certamente isso vai te auxiliar.
# 
# Veja um exemplo (no caso, para fazer sentido, leva os mesmos valores de um exemplo da documentação):

# In[84]:


from sympy.physics.continuum_mechanics.beam import Beam
E, I = symbols('E I') ## Símbolos para o Módulo de Elasticidade e o Momento de Inércia
R1, R2 = symbols('R1 R2') ## Símbolos para as forças
b = Beam(50, 20, 30) ## Criando a viga (comprimento, E, I)
b.apply_load(R1, 0, -1) ## Aplicando carregamentos (intensidade, início, ordem)
###
### Momentos, order = -2
### Forças Pontuais, order =-1
### Forças distribuídas linearmente, order = 0
### Veja os outros na documentação
###
b.apply_load(R1, 10, -1)
b.apply_load(R2, 30, -1)
b.apply_load(90, 5, 0, 23)
b.apply_load(10, 30, 1, 50)
b.load ## Carregamento


# In[81]:


b.shear_force() ## Força Cortante


# In[82]:


b.bending_moment() ## Momento Fletor


# In[86]:


p = b.draw()
p.show() ## Ilustração Gráfica


# In[85]:


b.solve_for_reaction_loads(R1, R2) ## Solucionando
b.plot_bending_moment() ## Plot Momento Fletor


# In[87]:


b.plot_shear_force() ## Plotando Força Cortante


# In[88]:


b.apply_support(50, 'pin') ## Criando apoios
b.apply_support(0, 'fixed')
b.apply_support(20, 'roller')
b.load


# In[89]:


p = b.draw()
p.show()

