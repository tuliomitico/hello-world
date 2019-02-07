def heapfica(vetor, n, i): 
    maior = i 
    esq = 2 * i + 1      
    dir = 2 * i + 2     
  

    if esq < n and vetor[i] < vetor[esq]: 
        maior = esq 
  
     
    if dir < n and vetor[maior] < vetor[dir]: 
        maior = dir 
  
    
    if maior != i: 
        vetor[i],vetor[maior] = vetor[maior],vetor[i] 
  
         
        heapfica(vetor, n, maior) 
  
 
def heapsort(vet): 
    n = len(vet) 
  
     
    for i in range(n, -1, -1): 
        heapfica(vet, n, i) 
  
    
    for i in range(n-1, 0, -1): 
        vet[i], vet[0] = vet[0], vet[i] 
        heapfica(vet, i, 0) 

a,b=map(int,input().split())
c=list(map(int,input().split()))
heapsort(c)
d,e=0,b
for i in range(a):
    d+=b//c[i]  

while d<e:
    b+=c[0]
    d=0
    for i in range(a):
        d+=b//c[i]
    if d>=e:
        print(b)
        break

