def romano_a_decimal(vec, primero):
    for i in range(len(vec)):
        if vec[i]=="I":
            vec[i] = 1
        elif vec[i]=="V":
            vec[i]=5 
        elif vec[i]=="X":
            vec[i]=10
        elif vec[i]=="L":
            vec[i]=50
        elif vec[i]=="C":
            vec[i]=100
        elif vec[i]=="D":
            vec[i]=500
        elif vec[i]=="M":
            vec[i]=1000
    if primero == len(vec):
        return 0
    elif (len(vec)-primero)>=3 and vec[primero]>=vec[primero+1]>=vec[primero+2]:
        aux=vec[primero]+vec[primero+1]+vec[primero+2]
        primero += 3
    elif (len(vec)-primero)>=3 and vec[primero]>vec[primero+1]<vec[primero+2]:
        aux=(vec[primero+2]-vec[primero+1])+vec[primero]
        primero += 3
    elif (len(vec)-primero)>=2 and vec[primero] == vec[primero+1]:
        aux=vec[primero]+vec[primero+1]
        primero +=2
    elif (len(vec)-primero)>=2 and vec[primero]<vec[primero+1]:
        aux=vec[primero+1]- vec[primero]
        primero +=2
    elif (len(vec)-primero)==1 and vec[primero-1]<vec[primero]:
        aux=vec[primero-1]-vec[primero]
        primero+=1
    elif (len(vec)-primero)==1 and vec[primero-1]>=vec[primero]:
        aux=vec[primero]
        primero+=1
    return aux + romano_a_decimal(vec,primero)
    
# DCCCXXXIX=839, CDXCIX=499, XCIX=99, XIX=19, LXXIV=74
print("resultado final: " , romano_a_decimal(["C", "D", "X","C", "I", "X"], 0))    
