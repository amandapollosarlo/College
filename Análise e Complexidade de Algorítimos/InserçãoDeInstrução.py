#caso médio
import time
import random 


x=10000
v=random.sample(range(10000),x)

#x=100
#v=random.sample(range(100),x)

#x=1000
#v=random.sample(range(1000),x)

#x=10000
#v=random.sample(range(10000),x)

def insertionSort(v):
  j=0
  for j in range(len(v)):
    chave = v[j]
    i = j-1
    while i>=0 and v[i] > chave:
      v[i+1]=v[i]
      i = i-1
    v[i+1]=chave
  return v

start = time.time()
v = insertionSort(v)
print(v)


end=time.time()
print(end-start)
