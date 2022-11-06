matriz = []

def operacion(t):
    for i in range(t):
        matriz.append([])
        for j in range(t):
            matriz[i].append(0)
    return matriz

def rellenar(t):
    matriz = operacion(t)
    for x in range(t):
        for y in range(t):
            matriz[x][y] = float(input("Introduce el valor de [" + str(x) + "][" + str(y) + "]= "))

def sarrus(t):
    for z in range(t-1):
        for x in range(1, t-z):
            if(matriz[z][z] !=0):
                pon = matriz[x+z][z] / matriz[z][z]
                for y in range(t):
                    matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*pon)

def determinante(t):
    det=1
    for x in range(t):
        det = matriz[x][x]*det
    print("El determinante de la matriz es =", det)

def im(t):
    for i in range(t):
        for j in range(t):
            print(matriz[i][j])
        print("\n")

t = input("Introduce el tamaño de la matriz: ")
n = int(t)
rellenar(n)
sarrus(n)
determinante(n)
