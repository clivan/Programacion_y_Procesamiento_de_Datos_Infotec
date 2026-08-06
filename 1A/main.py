Temperatura1=Temperatura2=Temperatura3=Temperatura4=Temperatura5=None


def menu1():
    print("===========================")
    print("Análisis de datos de temperatura")
    print("===========================")
    print("1. Capturar datos")
    print("2. Ejecutar análisis")
    print("3. Salir")

def op1():
    temp1=0.0
    temp2=0.0
    temp3=0.0
    temp4=0.0
    temp5=0.0
    print("Dame 5 valores de temperatura")
    aux=float(input())
    if (aux==float):
        temp1=aux
    else:
        aux=None
    aux=input()
    if (aux==float):
        temp2=aux
    else:
        aux=None
    aux=input()
    if (aux==float):
        temp3=aux
    else:
        aux=None
    aux=input()
    if (aux==float):
        temp4=aux
    else:
        aux=None
    aux=input()
    if (aux==float):
        temp5=aux
    else:
        aux=None
    return temp1, temp2, temp3, temp4, temp5

def op2(temp1, temp2, temp3, temp4, temp5):
    Vmin=0
    Vmax=0
    prom=0
    Ninv=0
    NOoR=0
    ssum=0.0
    if (temp1==None):
        print(f"Valor inválido")
        Ninv+=1
    if (temp2==None):
        print(f"Valor inválido")    
        Ninv+=1
    if (temp3==None):
        print(f"Valor inválido")
        Ninv+=1
    if (temp4==None):
        print(f"Valor inválido")
        Ninv+=1
    if (temp5==None):
        print(f"Valor inválido")
        Ninv+=1
    if (temp1<20 or temp1>50):
        temp1=0
        NOoR+=1
    if (temp2<20 or temp2>50):
        temp2=0
        NOoR+=1
    if (temp3<20 or temp3>50):
        temp3=0
        NOoR+=1
    if (temp4<20 or temp4>50):
        temp4=0
        NOoR+=1
    if (temp5<20 or temp5>50):
        temp5=0
        NOoR+=1
    if (temp1 != 0 or temp1 !=None):
        ssum+=temp1
        Vmin=temp1
        Vmax=temp1
    if (temp2 != 0 or temp2 !=None):
        ssum+=temp2
        if (temp2<Vmin):
            Vmin=temp2
        if (temp2>Vmax):
            Vmax=temp2
    if (temp3 != 0 or temp3 !=None):
        ssum+=temp3
        if (temp3<Vmin):
            Vmin=temp3
        if (temp3>Vmax):
            Vmax=temp3
    if (temp4 != 0 or temp4 !=None):
        ssum+=temp4
        if (temp4<Vmin):
            Vmin=temp4
        if (temp4>Vmax):
            Vmax=temp4
    if (temp5 != 0 or temp5 !=None):
        ssum+=temp5
        if (temp5<Vmin):
            Vmin=temp5
        if (temp5>Vmax):
            Vmax=temp5
    nn=Ninv+NOoR
    prom=ssum/nn
    return prom, Vmin, Vmax, Ninv, NOoR
    

a=0

nn=0
while (a!=3):
    a=int(input())
    print(a)
    if (a==1):
        temp1, temp2, temp3, temp4, temp5=op1()
        menu1()
    if (a==2):
        prom, Vmin, Vmax, Ninv, NOoR=op2(temp1, temp2, temp3, temp4, temp5)
        print(f"a. Promedio: ", prom)
        print(f"b. Valor mínimo: ", Vmin)
        print(f"c. Valor máximo: ", Vmax)
        print(f"d. Cantidad de valores inválidos (anomalías):", Ninv)
        print(f"e. Cantidad de valores fuera de rango (20° a 50°): ", NOoR)
        menu1()
        
    if (a!=0 and a!=1 and a!=2 and a!=3):
        print("Opción no válida")
