# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:28:48 2019

@author: Túlio
"""
#Algoritmo da Envoltória convexa utilizando o modelo de Graham que assintoticamente roda em O(nlogn),segundo os ensinamentos do livro de Udi Manber: A introduction to algorithms


from math import atan2,sqrt #Importa-se da biblioteca Math, sqrt que é raiz quadrada
                            #e o arcotangente para calcular o angulo formado por 3 pontos no plano tendo como base o eixo X.

def particao(v,esq,direi): #A receurisividade do qsort chama a particao toda vez ate esta tudo ordenado
    pivo=dist_seg(v[direi])
    pivo2=coef(v[direi])
    i=esq-1
    for j in range(esq,direi):
        if coef(v[j]) < pivo2 or (coef(v[j]) == pivo2 and dist_seg(v[j]) < pivo) :
            i+=1
            v[i],v[j] = v[j],v[i]
    v[i+1],v[direi]=v[direi],v[i+1]
    return i+1
    
    
def qsort(v,esq,direi): # QuickSort adaptado para encontrar em ordem crescente os angulos do arcotangente, em caso de ser igual, leva 
    while esq<direi:    # em consideracao a distancia de segmentos
        pi=particao(v,esq,direi)
        if pi - esq < direi - pi:
            qsort(v,esq,pi - 1)
            esq = pi + 1
        else:
            qsort(v,pi+1,direi)
            direi = pi - 1
    return v
    
def coef(x,y=None): # Esta funcao determina o angulo entre os pontos que eh a principal pivo do quicksort adaptado
  if y==None:
    y=ancora
  ys=(x[1]-y[1])
  xs=(x[0]-y[0])
  angulo=atan2(ys,xs)
  return angulo

def orientacao(p,q,r): #funcao para encontrar a orientacao dos segmentos de retas formadas entre os pontos, dando valor negativo eh anti horario
                       # dando 0 eh colinear, positivo horario.
  val = (q[0] - p[0]) * (r[1] - p[1]) \
      - (q[1] - p[1]) * (r[0] - p[0])
  return val

def dist_seg(a,b=None): # Essa distancia de segmento irá servir como segundo argumento na adaptação do quicksort para a construção da
  if b==None:           #envoltoria
    b=ancora
  bs=(a[1]-b[1])
  a_s=(a[0]-b[0])
  return bs**2 + a_s**2

def tupla_min(arr): #Funcao utilizada para encontrar o ponto mais extremo, nesse caso maior y e menor x.
  ymin,xmax=arr[0][1],arr[0][0]
  for i in range(1,len(arr)):
    y=arr[i][1]
    x=arr[i][0]
    if  x < xmax or (xmax == x and y < ymin):
      ymin,xmax=arr[i][1],arr[i][0]
  return xmax,ymin

def convexa(v):
  global ancora #Cria-se uma var global para utilizacao em algumas funcoes. Ex: dit_seg,coef
  ancora = tupla_min(v) #Essa variavel vira o ponto mais extremo do plano
  ordenado=qsort(v,0,len(v)-1) #cria um vetor ordenado segundo a distancia e o angulo formado entre os pontos
  del ordenado[ordenado.index(ancora)] #retira-se a var ancora
  envo=[ancora,ordenado[0]] #cria um vetor com dois valores para a construcao do menor poligono possivel, o triangulo.
  m=len(envo) #salva o tamanho desse poligono
  for s in range(1,len(ordenado)):
    
    while orientacao(envo[m-2],envo[m-1],ordenado[s])<=0: #percorre as listas envo e ordenado 
      del envo[m-1]                                       #procurando as envoltorias q abrange todos os pontos
      m=len(envo) #atualiza o tamanho
      #if len(hull)<2: break
    envo.append(ordenado[s]) #adiciona os valores ja computados
    m=len(envo) #novamente atualiza  os tamanhos
  return envo #retorna os pontos que formam a envoltoria convexa


def dist_seg2(x,y): #Funcao para calcular a distancia entre dois pontos no plano
  ys=(x[1]-y[1])
  xs=(x[0]-y[0])
  return sqrt(ys**2+xs**2)

num=int(input())
while num!=0:
    z=[]
    for i in range(num):
    	x,y=map(int,input().split())
    	tup=(x,y)
    	z.append(tup)
    envoltoria=convexa(z)
    j=0
    j+=dist_seg2(envoltoria[0],envoltoria[1])
    for i in range(1,len(envoltoria)):
        if i<len(envoltoria)-1:
            j+=dist_seg2(envoltoria[i],envoltoria[i+1])
        else:
            j+=dist_seg2(envoltoria[0],envoltoria[len(envoltoria)-1])

    print("Tera que comprar uma fita de tamanho %.2f." %j)
    num=int(input())
