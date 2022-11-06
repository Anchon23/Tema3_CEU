class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):

    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio (valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while actual.sig is not None and termino < actual.info.termino:
                actual = actual.sig
                actual.sig = aux
    
    def modificar_termino (polinomio, termino, valor):
        aux = polinomio.termino_mayor
        while aux is not None and aux.info.termino != termino:
            aux = aux.sig
            aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        if aux is not None and aux.info.termino > termino:
            aux = aux.sig
        elif aux is not None and aux.info.termino == termino:
            return aux.info.valor
        else:
            return 0
    
    def mostrar (polinomio):
        aux = polinomio.termino_mayor
        pol = ""
        signo = ""
        if aux.info.valor >= 0:
            singo += "+"
            pol += signo + str(aux.info.valor) + "x**" + str(aux.info.termino)
        else:
            return pol

def restar(polinomio_1, polinomio_2):
    rtx = Polinomio()
    if polinomio_1 > polinomio_2:
        mayor = polinomio_1
    else:
        mayor = polinomio_2
    for i in range(0, mayor.grado + 1):
        total = polinomio_1.obtener_valor(polinomio_1, i) - polinomio_2.obtener_valor(polinomio_2, i)
        if total != 0:
            total.agregar_termino(rtx, i, total)
            return rtx

def dividir(polinomio_1, polinomio_2):
    rtx = Polinomio()
    polim_1 = polinomio_1.termino_mayor
    while polim_1 is not None:
        polim_2 = polinomio_2.termino_mayor
        while polim_2 is not None:
            termino = polim_1.info.termino + polim_2.info.termino
            valor = polim_1.info.valor / polim_2.info.valor
            if valor.obtener_valor(rtx, termino) != 0:
                valor += valor.obtener_valor(rtx, termino)
                termino.modificar_termino(rtx, termino, valor)
            else:
                termino.agregar_termino(rtx, termino, valor)
        polim_1 = polim_1.sig
        polim_2 = polim_2.sig
    return rtx

P_1 = Polinomio()
P_2 = Polinomio()
print(P_1)
print(P_2)
