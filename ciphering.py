import random

def przygotowanie(tekst):
	newtekst=""
	for i in tekst:
		if ord(i)>=65 and ord(i)<=90:
			newtekst = newtekst+chr(ord(i)+32)
		if ord(i)>=97 and ord(i)<=122:
			newtekst = newtekst + i
	return (newtekst)
	
txt = input("Podaj tekst: ")
print (przygotowanie(txt))


def cezar(text, move):
	text=przygotowanie(text)
	newtekst=""
	for i in text:
		z=chr(ord(i)+move)
		if ord(z)>122:
			z=chr(ord(z)-26)
		newtekst = newtekst + z
	return (newtekst)

print (cezar(txt,2))

def deCezar(text, move):
	text=przygotowanie(text)
	newtxt=""
	for i in text:
		z=chr(ord(i)-move)
		if ord(z)<97:
			z=chr(ord(z)+26)
		newtxt=newtxt+z
	return (newtxt)
	
print (deCezar(cezar(txt,5),5))

def alfabet():
	alf=[]
	for i in range(97,123):
		alf.append(chr(i))
	random.shuffle(alf)
	return (alf)
	
al=alfabet()
print (al)
	
def podstawieniowy(tekst, alfabe):
	tekst=przygotowanie(tekst)
	new=""
	for i in tekst:
		z=alfabe[ord(i)-97]
		new=new + z
	return (new)
	
kod = podstawieniowy(txt,al)
print (kod)

def dePodstawieniowy(tekst,alfa):
	tekst=przygotowanie(tekst)
	new=""
	for i in tekst:
		z=chr(alfa.index(i)+97)
		new=new+z
	return (new)
	
print (dePodstawieniowy(kod,al))

def zKluczem(text, klucz):
	text=przygotowanie(text)
	klucz=przygotowanie(klucz)
	new=""
	a=len(klucz)
	b=0
	for i in text:
		z=ord(i)+ord(klucz[b])-96
		if z>122:
			z=z-26
		new=new+chr(z)
		b=(b+1)%a
	return (new)
	
ala= zKluczem(txt,"boa")
print (ala)

def deZKluczem(tekst, klucz):
	new=""
	a=len(klucz)
	b=0
	for i in tekst:
		z=ord(i)-ord(klucz[b])+96
		if z<97:
			z=z+26
		new=new+chr(z)
		b=(b+1)%a
	return (new)
		
print (deZKluczem(ala,"boa"))