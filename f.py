import string, random
def kradnijkarte(numer):
    plik = open('dane.txt','w+')
    plik.write(numer)
    print (plik.read())
    plik.close()

kradnijkarte("ekhem")

def generatorhasel(dlugosc):
    if dlugosc < 1:
        return ''
    all = string.ascii_letters + string.digits
    return(''.join(random.choices(all, k=dlugosc)))






        

        


