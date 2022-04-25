matriz=[
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 3]
    ]
def salida_laberinto(mat, fila, columna, pos=[]):
    if fila>=0 and fila<=len(mat)-1 and columna>=0 and columna<=len(mat)-1:
        if mat[fila][columna]==3:
            print("salida") 
            pos.append([fila, columna])
            print(pos)
            pos.pop()  
        elif mat[fila][columna]==0:
            print("posicion: "+str(fila)+str(columna))
            pos.append([fila, columna])
            matriz[fila][columna]=2
            salida_laberinto(mat, fila, columna+1, pos)
            salida_laberinto(mat, fila+1, columna, pos)  
            salida_laberinto(mat, fila, columna-1, pos) 
            salida_laberinto(mat, fila-1, columna, pos)
            pos.pop()
            mat[fila][columna]==0
      
print(salida_laberinto(matriz, 0, 0))