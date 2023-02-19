from colorama import Back, init

# * Creamos el laberinto según los muros que le mandamos por parametros
def init_laberinto(dimension, muro):
    # * Creamos una lista vacía para añadir las filas del laberinto.
    laberinto = []
    # * Recorrido de las filas del laberinto
    for i in range(dimension):
        # * Creamos una lista vacía para añadir las laberinto[i][j]s de la fila.
        fila = []
        # * Recorrido de las columnas del laberinto.
        for j in range(dimension):
            # * Si en esa laberinto[i][j] hay un muro
            if tuple([i, j]) in muro:
                fila.append('X')
            # * Si no
            else:
                fila.append(' ')
            if [i, j] == [dimension-1, dimension-1]:
                fila[j] = 'S'
        laberinto.append(fila)
    return laberinto

# * recorremos el laberinto y guardamos la dirección que toma en una lista de pasos
def recorre_laberinto(laberinto):
    # * Fila y columnas iniciales
    fila = columna = 0
    # * Lista de pasos
    n = len(laberinto)
    posiciones = []
    pasos = ['']
    encontrado = False
    #* mientras que no encontremos la salida
    while (encontrado == False):
        posiciones.append((fila, columna))
        laberinto[fila][columna] = '*'
        # * si el paso anterior no es arriba, la fila de abajo es menor que el maximo, y la siguiente laberinto[i][j] no es un muro
        if (pasos[-1] != 'Arriba') and (fila + 1 < n) and (laberinto[fila + 1][columna] != 'X') and (laberinto[fila + 1][columna] != '*'):
            fila += 1
            pasos.append('Abajo')
        # * si el paso anterior no es abajo, la fila de arriba es mayor que 0 y la laberinto[i][j] de la fila de arriba no es un muro
        elif (pasos[-1] != 'Abajo') and (fila - 1 >= 0) and (laberinto[fila - 1][columna] != 'X') and (laberinto[fila - 1][columna] != '*'):
            fila -= 1
            pasos.append('Arriba')
        # * si el paso anterior no es izquierda, la columna de la derecha es mayor que el maximo y la laberinto[i][j] de la columna de la derecha no es un muro
        elif (pasos[-1] != 'Izquierda') and (columna + 1 < n) and (laberinto[fila][columna + 1] != 'X') and (laberinto[fila][columna + 1] != '*'):
            columna += 1
            pasos.append('Derecha')
        # * si el paso anterior no es derecha, la columna de la izquierda es mayor que 0, y la laberinto[i][j] de la izquierda no es un muro
        elif (pasos[-1] != 'Derecha') and (columna - 1 >= 0) and (laberinto[fila][columna - 1] != 'X') and (laberinto[fila][columna - 1] != '*'):
            print(laberinto[fila][columna - 1])
            columna -= 1
            pasos.append('Izquierda')
        # * si no hay salida retrocede y elige otro camino
        else:
            pasos.append('No hay salida')
            pasos, posiciones = retroceder(laberinto, pasos, posiciones)
            p = posiciones[-1]
            fila = p[0]
            columna = p[1]
        #* si encontramos la casilla de salida
        if laberinto[fila][columna] == 'S':
            encontrado = True
            pasos.pop(0)
    return pasos, posiciones

# * retrocede las casillas necesarias para encontrar otra posible ruta
def retroceder(laberinto, pasos, posiciones):
    #* sacamos la entrada 'No hay salida' de los pasos y las posiciones
    pasos.pop(0)
    n = len(laberinto)
    k = len(posiciones) - 1
    #* guardamos la ultima posicion de la lista
    p = posiciones[-1]
    i = p[0]
    j = p[1]
    encontrado = False
    while k > 0 and encontrado == False:
        encontrado = False
        anterior = pasos[-2]
        #* vengo de la izquierda
        if anterior == 'Izquierda':
            #* compruebo: si no he pasado por la derecha y si no hay un muro a la derecha
            if laberinto[i][j + 1] != '*' and laberinto[i][j + 1] != 'X' and (j + 1) < n:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Derecha')
            #* compruebo: si no he pasado por abajo y si no hay un muro abajo
            elif laberinto[i + 1][j] != '*' and laberinto[i + 1][j] != 'X' and (i + 1) < n:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Abajo')
            #* compruebo: si no he pasado por arriba y si no hay un muro arriba
            elif laberinto[i - 1][j] != '*' and laberinto[i - 1][j] != 'X' and (i - 1) >= 0:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Arriba')
            else:#* voy a la izquierda
                j -= 1
        #* vengo de la derecha
        elif anterior == 'Derecha':
            #* compruebo: si no he pasado por la derecha y si no hay un muro a la derecha
            if laberinto[i][j + 1] != '*' and laberinto[i][j + 1] != 'X' and (j + 1) < n:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Derecha')
            #* compruebo: si no he pasado por abajo y si no hay un muro abajo
            elif laberinto[i + 1][j] != '*' and laberinto[i + 1][j] != 'X' and (i + 1) < n:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Abajo')
            #* compruebo: si no he pasado por arriba y si no hay un muro arriba
            elif laberinto[i - 1][j] != '*' and laberinto[i - 1][j] != 'X'and (i - 1) >= 0:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Arriba')
            else:#* voy a la izquierda
                j -= 1
        #* vengo de arriba
        elif anterior == 'Arriba':
            #* compruebo: si no he pasado por la derecha y si no hay un muro a la derecha
            if laberinto[i][j + 1] != '*' and laberinto[i][j + 1] != 'X' and (j + 1) < n:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Derecha')
            #* compruebo: si no he pasado por abajo y si no hay un muro abajo
            elif laberinto[i + 1][j] != '*' and laberinto[i + 1][j] != 'X' and (i + 1) >= 0:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Arriba')
            #* compruebo: si no he pasado por la izquierda y si no hay un muro a la izquierda
            elif laberinto[i][j + 1] != '*' and laberinto[i][j + 1] != 'X' and (j + 1) >= 0:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Izquierda')
            else:#* bajo
                i += 1
        #* vengo de abajo
        elif anterior == 'Abajo':
            #* compruebo: si no he pasado por la derecha y si no hay un muro a la derecha
            if laberinto[i][j + 1] != '*' and laberinto[i][j + 1] != 'X' and (j + 1) < n:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Derecha')
            #* compruebo: si no he pasado por abajo y si no hay un muro abajo
            elif laberinto[i + 1][j] != '*' and laberinto[i + 1][j] != 'X' and (i + 1) < n:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Abajo')
            #* compruebo: si no he pasado por la izquierda y si no hay un muro a la izquierda
            elif laberinto[i][j - 1] != '*' and laberinto[i][j - 1] != 'X' and (j - 1) >= 0:
                pasos.pop(-1)
                encontrado = True
                pasos.append('Izquierda')
            else:#* subo
                i -= 1
        #* no encontramos otra ruta
        if encontrado == False:
            #* siguiente elemento
            pasos.pop(-1)
            posiciones.pop(-1)
        #* encontramos otra ruta
        else:
            posiciones[k] = (i, j)
        k -= 1
    return pasos, posiciones

# * muestra el laberinto por consola
def mostrar_laberinto(laberinto, posiciones, pasos):
    p = 0
    #* marco las posiciones por donde pasa la solución
    while p < len(posiciones):
        pos = posiciones[p]
        a = pos[0]
        b = pos[1]
        laberinto[a][b] = 'P'
        p += 1
    #* muestro el laberinto por la terminal
    for i, fila in enumerate(laberinto):
        for j, casilla in enumerate(fila):
            if casilla == 'P' or casilla == 'S':
                print(Back.GREEN+"  ", end="")
            elif casilla == 'X':
                print(Back.RED+"  ", end="")
            else:
                print(Back.LIGHTBLACK_EX+"  ", end="")
        print()

if __name__ == '__main__':
    init()
    dim = 5
    muros = ((1,0), (1,1), (1,2), (1,4), (3,0), (3,2), (3,4), (4,2))
    laberinto = init_laberinto(dim, muros)
    pasos, direcciones = recorre_laberinto(laberinto)
    mostrar_laberinto(laberinto, direcciones, pasos)
    print(Back.RESET+"Solucion: ",pasos)