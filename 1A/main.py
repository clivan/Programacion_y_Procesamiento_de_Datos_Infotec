Temperatura1=Temperatura2=Temperatura3=Temperatura4=Temperatura5=None

def isfloat(num):
    if num[:1] == '-':
        resto = num[1:]
    else:
        resto = num
    if resto.replace(".", "", 1).isdigit():
        isf = True
    else:
        isf = False
    return isf

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
    aux=input()
    if isfloat(aux):
        temp1=float(aux)
    else:
        temp1=None
    aux=input()
    if isfloat(aux):
        temp2=float(aux)
    else:
        temp2=None
    aux=input()
    if isfloat(aux):
        temp3=float(aux)
    else:
        temp3=None
    aux=input()
    if isfloat(aux):
        temp4=float(aux)
    else:
        temp4=None
    aux=input()
    if isfloat(aux):
        temp5=float(aux)
    else:
        temp5=None
    return temp1, temp2, temp3, temp4, temp5

def op2(temp1, temp2, temp3, temp4, temp5):
    Vmin=0
    Vmax=0
    prom=0
    Ninv=0
    NOoR=0
    Nval=0
    ssum=0.0
    if (temp1==None):
        print(f"Valor inválido")
        Ninv+=1
    elif (temp1<20 or temp1>50):
        NOoR+=1
    else:
        ssum+=temp1
        if (Nval==0):
            Vmin=temp1
            Vmax=temp1
        else:
            if (temp1<Vmin):
                Vmin=temp1
            if (temp1>Vmax):
                Vmax=temp1
        Nval+=1
    if (temp2==None):
        print(f"Valor inválido")
        Ninv+=1
    elif (temp2<20 or temp2>50):
        NOoR+=1
    else:
        ssum+=temp2
        if (Nval==0):
            Vmin=temp2
            Vmax=temp2
        else:
            if (temp2<Vmin):
                Vmin=temp2
            if (temp2>Vmax):
                Vmax=temp2
        Nval+=1
    if (temp3==None):
        print(f"Valor inválido")
        Ninv+=1
    elif (temp3<20 or temp3>50):
        NOoR+=1
    else:
        ssum+=temp3
        if (Nval==0):
            Vmin=temp3
            Vmax=temp3
        else:
            if (temp3<Vmin):
                Vmin=temp3
            if (temp3>Vmax):
                Vmax=temp3
        Nval+=1
    if (temp4==None):
        print(f"Valor inválido")
        Ninv+=1
    elif (temp4<20 or temp4>50):
        NOoR+=1
    else:
        ssum+=temp4
        if (Nval==0):
            Vmin=temp4
            Vmax=temp4
        else:
            if (temp4<Vmin):
                Vmin=temp4
            if (temp4>Vmax):
                Vmax=temp4
        Nval+=1
    if (temp5==None):
        print(f"Valor inválido")
        Ninv+=1
    elif (temp5<20 or temp5>50):
        NOoR+=1
    else:
        ssum+=temp5
        if (Nval==0):
            Vmin=temp5
            Vmax=temp5
        else:
            if (temp5<Vmin):
                Vmin=temp5
            if (temp5>Vmax):
                Vmax=temp5
        Nval+=1
    if (Nval==0):
        prom=0
    else:
        prom=ssum/Nval
    return prom, Vmin, Vmax, Ninv, NOoR
    
a=0
nn=0
menu1()
while (a!=3):
    a=int(input())
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
