#https://github.com/AllenDowney/ThinkPython/tree/master
import math

def fattoriale(n): 
    if not isinstance(n, int):
        print('Il fattoriale è definito solo per numeri interi.')
        return None
    elif n < 0:
        print('Il fattoriale è definito solo per numeri interi positivi')
        return None
    elif n==0:
        return 1
    else:
        return n * fattoriale(n-1)

def fibonacci(n):
    """i=0
    fibonacci = []
    for i in range(n):
        print(i)
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    """
    memo = {0:0, 1:1}
    if n in memo:
        return memo[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    memo[n]=res
    return res
        

def MCD():
    return 

def shell_command():
    while True:
        riga = input('> ')
        if riga == 'exit':
            break
    print('Finito!')
     
def upperc(lista):
    res = []
    for carattere in lista:
        res.append(carattere.capitalize())
    return res

def totale_lista(lista):
    somma=0
    for numero in lista:
        somma += numero
    print(somma)
    return somma 

def ordina_lista(t):
    print(t)
    tres = t[:]
    tres.sort()
    print(tres)
    return tres

def somma_nidificata(t):
    res = 0
    app = []
    for val in t:
        if type(val)=='int':
            app.append(val)
        else:
            app = app + val
    print(app)
    for val in app:
        res = res + val
    
    return res

def somma_cumulata(t):
    app = []
    i = 0
    print('Lista: ',t)
    for i in range(len(t)):
        print('Indice: ',i,' valore: ',t[i])
        if i == 0:
            app.append(t[i])
        else:
            app.append(t[i] + app[i-1])    
    return app

def mediana(t):
    lunghezza = len(t)
    return t[1:lunghezza-1]

def bifronte(t):
    
    #acetone = enoteca

    return

def dizionario_inglese():
    dizionario = dict()
    dizionario['one']='uno'
    dizionario['two']='due'
    dizionario['three']='tre'
    return dizionario

def dizionario_credenziali(username, password):
    cred = dict()
    cred['username'] = username
    cred['password'] = password
    return cred

"""
    Conta la frequenza dei caratteri in una stringa
"""
def istogramma(t):
    d = dict()
    for l in t:
        l = l.lower()
        d[l] = d.get(l,0)
        d[l] += 1
    """ 
    for l in t:
        l = l.lower()  
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    """
    return d

"""
    stampa l'istogramma in modo ordinato
"""
def stampa_istogramma(isto):
    for key in sorted(isto):
        print(key,' = ',isto.get(key))   
        
"""lookup_inverso
    cerca un valore nel dizionario. Se lo trova restituisce la chiave del primo valore uguale intercettato
"""         
def lookup_inverso(d,v):
    for k in d:
        if v == d[k]:
            return k
    raise LookupError('Valore non trovato nel dizionario') 

   
def lookup_inverso_dizionario(d,v):
    res = dict()
    for k in d:
        if( v == d[k] ):
            res[k] = d[k]
    return res
            
def dizionario_inverso(d):
    inverso = dict()
    for k in d:
        valore = d[k]
        if valore not in inverso:
            inverso[valore] = [k]
        else:
            inverso[valore].append(k)
    return inverso

def conteggio_caratteri_files(f):
    fi = open(f, "r")
    lettura = fi.read()
    d = dict()
    
    for i in range(len(lettura)):
        k = lettura[i].lower()
        d[k] = d.get(k,0)
        d[k] += 1
    
    return d  

""" Funzione che verifica la presenza di duplicati in un lista"""

def ha_duplicati(l):
    """
    app =[]
    for v in l:
        if v in app:
            return True
        else:
            app.append(v)
    return False
    """
    """
    d = dict()
    for v in l:
        print(v)
        if v in d:
            d[v] += 1
        else:
            d[v] = d.get(v,0)
    return d
    """
    
    """
    d = dict()
    for v in l:
        if v in d:
            return True
        d[v] = True
    return False
    """
    return len(set(l))<len(l)

def min_max(t):
    return min(t), max(t)

def quoziente_resto(dividendo, divisore):
    quoziente = dividendo // divisore
    resto = dividendo % divisore 
    return quoziente, resto

def decimale_binario(n):
    """ Versione 1 con lista
    resto = list()
    divisore = int(n)
    DIVIDENDO = 2
    quoziente = divisore
    while quoziente != 0:
        resto.append(quoziente % DIVIDENDO)
        quoziente = quoziente // DIVIDENDO
    resto.reverse()
    #res = "".join(map(str, resto))
    res = "".join(str(_) for _ in resto)
    return res
    """
    
    """ Versione 2 con stringa"""
    resto = ''
    divisore = int(n)
    quoziente = divisore
    DIVIDENDO = 2
    
    while quoziente != 0:
        resto = resto + str(quoziente % DIVIDENDO)
        quoziente = quoziente // DIVIDENDO
    
    res = resto[::-1] #invertiamo la stringa
    print(res)