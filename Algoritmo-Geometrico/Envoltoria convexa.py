# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:28:48 2019

@author: Túlio
"""
from math import atan2,sqrt

def particao(v,esq,direi):
    pivo=dist_seg(v[direi])
    pivo2=coef(v[direi])
    i=esq-1
    for j in range(esq,direi):
        if coef(v[j]) < pivo2 or (coef(v[j]) == pivo2 and dist_seg(v[j]) < pivo) :
            i+=1
            v[i],v[j] = v[j],v[i]
    v[i+1],v[direi]=v[direi],v[i+1]
    return i+1
    
    
def qsort(v,esq,direi):
    while esq<direi:
        pi=particao(v,esq,direi)
        if pi - esq < direi - pi:
            qsort(v,esq,pi - 1)
            esq = pi + 1
        else:
            qsort(v,pi+1,direi)
            direi = pi - 1
    return v
    
def coef(x,y=None):
  if y==None:
    y=ancora
  ys=(x[1]-y[1])
  xs=(x[0]-y[0])
  angulo=atan2(ys,xs)
  return angulo

def orientacao(p,q,r):

  val = (q[0] - p[0]) * (r[1] - p[1]) \
      - (q[1] - p[1]) * (r[0] - p[0])
  return val

def dist_seg(a,b=None):
  if b==None:
    b=ancora
  bs=(a[1]-b[1])
  a_s=(a[0]-b[0])
  return bs**2 + a_s**2

def tupla_min(arr):
  ymin,xmax=arr[0][1],arr[0][0]
  for i in range(1,len(arr)):
    y=arr[i][1]
    x=arr[i][0]
    if  x < xmax or (xmax == x and y < ymin):
      ymin,xmax=arr[i][1],arr[i][0]
  return xmax,ymin

def convexa(v):
  global ancora 
  ancora = tupla_min(v)
  ordenado=qsort(v,0,len(v)-1)
  del ordenado[ordenado.index(ancora)]
  envo=[ancora,ordenado[0]]
  m=len(envo)
  for s in range(1,len(ordenado)):
    
    while orientacao(envo[m-2],envo[m-1],ordenado[s])<=0:
      del envo[m-1]
      m=len(envo)
      #if len(hull)<2: break
    envo.append(ordenado[s])
    m=len(envo)
  return envo
  
def dist_seg2(x,y):
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
