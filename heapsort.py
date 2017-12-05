import random
tablica=[]
a=10
for i in range(a):
	tablica.append(i)
random.shuffle(tablica)
print (tablica)

def heapify(tab, x, size):
	left=2*x+1
	right=2*x+2
	largest=x
	if left<size and tab[left]>tab[x]:
		largest=left
	if right<size and tab[right]>tab[largest]:
		largest=right
	if largest!=x:
		tab[x],tab[largest]=tab[largest],tab[x]
		heapify(tab, largest, size)
	
def build_heap(tab):
	heap_size=len(tab)
	for j in range(int((len(tab)-1)/2),-1,-1):
		heapify(tab, j, heap_size)

def heapsort(tab):
	build_heap(tab)
	heap_size=len(tab)
	for k in range(len(tab)-1,0,-1):
		tmp=tab.pop(0)
		tab.insert(k,tmp)
		heap_size=heap_size-1
		heapify(tab,0,heap_size)
		
		
heapsort(tablica)
print (tablica)