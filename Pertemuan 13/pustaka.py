def ganjil_genap(bilangan):
    if(bilangan % 2 ==0):
        return True
    else:
        return False

def faktorial(x):
    fX=1
    for i in range (1,x+1):
        fX *=i
    return fX
