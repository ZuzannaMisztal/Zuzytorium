import random
tablica=[]
a=1002
for i in range(a):
	tablica.append(i)
random.shuffle(tablica)
print (tablica)

def partition(tab,low,high):
	pivot=tab[high]
	l=low
	h=high-1
	while l<=h:
		while tab[l]<pivot:
			l+=1
		if l<h:
			while tab[h]>pivot and h>l:
				h-=1
		tab[l],tab[h]=tab[h],tab[l]
		l+=1
	tab[high],tab[h]=tab[h],tab[high]
	if l-1>h:
		return l-1
	return h

def quicksort(tab, left, right):
	part=partition(tab,left,right)
	if (left<part-1):
		quicksort(tab,left,part-1)
	if (part+1<right):
		quicksort(tab,part+1,right)
		
	return tab
	
def quick(tab):
	quicksort(tab,0,len(tab)-1)
	return tab
print (quick(tablica))