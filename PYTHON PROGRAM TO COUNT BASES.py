Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> DNA =("AAATTTGGGCC")
>>> A=0
>>> T=0
>>> G=0
>>> C=0
>>> for i in DNA:
	if i =="A":
		A=A+1
	elif i=="T":
		T=T+1
	elif i=="C":
		C=C+1
	elif i=="G":
		G=G+1
	else:
		pass
	return A,T,G,C
SyntaxError: 'return' outside function
>>> return A,T,G,C
SyntaxError: 'return' outside function
>>> 