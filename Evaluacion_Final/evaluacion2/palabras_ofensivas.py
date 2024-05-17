from urllib import request
from urllib.error import URLError

palabras_ofensivas=['conño', 'puta','pinche']
palabras_encontradas=[]
cant_po=0

def ver_po_en_la_web(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('La url '+ url + ' no existe!!')
    else:
        contenido= f.read()
        aux= contenido.split()
        for l in palabras_ofensivas:
            for con in aux:
                if l in con.decode():
                    palabras_encontradas.append(l)



        return palabras_encontradas
    



