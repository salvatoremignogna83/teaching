import turtle
import tartaruga
import funzioni

#n = input('Inserisci il numero del quale calcolare il fattoriale\n')
#print(funzioni.fattoriale(n))

#prova funzione somma_cumulata(t)
#t = [1,2,3,4,5]
#s = funzioni.somma_cumulata(t)
#print(s)

#prova funzione somma_nidificata(t)
#t = [[1,2],[1,2,3],[2,3]]
#print(t)
#res = funzioni.somma_nidificata(t)
#print(res)

#t=[1,2,3,4]
#print(funzioni.mediana(t))

"""
    
d = funzioni.traduzione_italiano_inglese()
print(d)
print(d['one'])

credenziali = funzioni.dizionario_credenziali('salvo@gmail.com','ApplePix01')
print(credenziali)
print(credenziali['password'])
print('username' in credenziali)
valori_dizionario = credenziali.values()
print(valori_dizionario)
print('salvo@gmail.co' in valori_dizionario)
for value in credenziali:
    print(value)
    print('Chiave: ',value,' Valore: ',credenziali[value])

"""

""" ISTOGRAMMA 
stringa = 'Attributo di cosa o persona che ha due fronti, due facce e particolarmente, in latino (bifrons), soprannome di Giano, che si rappresentava con due volti per significare la sua sapienza e la sua cognizione del passato e del futuro.'      

isto = funzioni.istogramma(stringa)
print(isto)

funzioni.stampa_istogramma(isto)
"""  

"""LOOKUP_INVERSO 
d = {'1' : 'a','2' : 'b','3' : 'c'}
print(funzioni.lookup_inverso(d,'d'))
"""

""" LOOKUP_INVERSO_DIZIONARIO
d = {'1' : 'a','2' : 'b','3' : 'c','lettera':'a','lettera2':'c'}
print(funzioni.lookup_inverso_dizionario(d,'b'))
"""

""" DIZIONARIO_INVERSO
d = {'1' : 'a','2' : 'b','3' : 'c','lettera':'a','lettera2':'c'}
print(d)
print(funzioni.dizionario_inverso(d))
"""

""" SUCCESSIONE DI FIBONACCI 
n = int(input('Inserisci n: '))
print(funzioni.fibonacci(n))
"""

""" CONTEGGIO CARATTERI FILES
file_name = input('Inserisci il nome del file: ')
conteggio = funzioni.conteggio_caratteri_files(file_name)
print(conteggio)
"""

""" HA_DUCPLICATI
lista = [1,'a',2,3,44,'c']
print(funzioni.ha_duplicati(lista))
"""

""" MIN_MAX
lista = [1,5,2,10,11,3]
min, max = funzioni.min_max(lista)
print(min,max)
"""
""" quoziente_resto 
dividendo  = int(input('Inserisci il dividendo: '))
divisore = int(input('Inserisci il divisore: '))
quoziente, resto = funzioni.quoziente_resto(dividendo, divisore)
print('Quoziente: ',quoziente)
print('Resto: ',resto)
"""

"""decimale_binario"""
n = input('Inserisci il numero da convertire: ')
conv =funzioni.decimale_binario(n)
print(conv)