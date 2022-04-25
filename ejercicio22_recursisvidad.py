vector=["pistola", "cadena", "latigo", "resortera", "soga"]
def usar_fuerza(vec,indice):
    if indice == len(vec):
        print("el sable de luz no se encuentra en la mochila")
        return -1
    elif vec[indice]=="sable de luz":
        return  print(f"se encontro el sable de luz despues de sacar {indice} objetos")
    indice += 1
    usar_fuerza(vec,indice)
    
print(usar_fuerza(vector,0))