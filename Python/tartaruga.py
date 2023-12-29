import turtle
import math

def quadrato(t, lunghezza):
    """ Documentazione funzione quadrato, con le triple doppie virgolette
     è possibile introdurre commenti su più linee """
    for i in range(4):
        t.fd(lunghezza)
        t.lt(90)

def poligono(t, lunghezza, n):
    for i in range(n):
        t.fd(lunghezza)
        t.lt(360/n)

def cerchio(t,r):
    circonferenza = 2 * r * math.pi
    n = 50
    l = circonferenza / n
    poligono(t,l,n)

def disegna_tartaruga(t,f,l,n,r):
    print(t)
    if(f == 'quadrato'):
        quadrato(t,l)
    if( f == 'poligono'):
        poligono(t,l,n)
    if( f == 'cerchio'):
        cerchio(t,r)
    
#t = turtle.Turtle()
#disegna_tartaruga(t,f = 'quadrato',l = 50,n = 0,r = 0)
#disegna_tartaruga(t,f = 'poligono',l = 50,n = 18, r = 0)
#disegna_tartaruga(t,f = 'cerchio',l = 0,n = 0,r = 50)

#turtle.mainloop()

