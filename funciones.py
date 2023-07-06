#IMPORTACIONES
from numpy import zeros
from os import system
#VARIABLES
ubicaciones = zeros((10,10),int)
cont=1
for x in range(10):
    for y in range(10):
        ubicaciones[x][y] = cont
        cont+=1

lista_rut = []
lista_asiento=[]
lista_venta=[]
cont_platinum=0
cont_gold=0
cont_silver=0

#FUNCIONES
def lp():
    system('cls')

def validar_opcion():
    while True:
        try:
            opcion = int(input("INGRESE UNA OPCIÓN\n\t>>> "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                lp()
                print("ERROR! DEBES INGRESAR UNA OPCIÓN VALIDA")
        except:
            lp()
            print("ERROR! DEBES INGRESAR UNA OPCIÓN VALIDA!")

def validar_cant_asientos_disponibles():
    k=0
    for x in range(10):
        for y in range(10):
            if ubicaciones[x][y] == "X":
                k+=1
            else:
                pass
    return k 

def validar_entradas():
    while True:
        try:
            cant_entradas = int(input("INGRESE CANTIDAD DE ENTRADAS QUE DESEA COMPRAR\n\t>>> "))
            if cant_entradas>=1 and cant_entradas<=3:
                lp()
                break
            else:
                lp()
                print("ERROR! DEBE INGRESAR UNA CANTIDAD DE ENTRADAS ENTRE 1 Y 3")
        except:
            lp()
            print("ERROR! DEBE INGRESAR UNA CANTIDAD DE ENTRADAS VALIDA!")
    return cant_entradas

def mostrar_ubicaciones():
    print("\n\tESCENARIO\n")
    for x in range(10):
        for y in range(10):
            if x<1:
                print("  ",ubicaciones[x][y],end=" ",sep=" ")
            else:
                print(" ",ubicaciones[x][y],end=" ")
        print()
    print()

def validar_rut():
    while True:
        try:
            rut=int(input("INGRESE RUT SIN PUNTOS, SIN GUIÓN NI DIGITO VERIFICADOR\n\t>>> "))
            if rut<99999999 and rut>4000000:
                if rut not in lista_rut:
                    lista_rut.append(rut)
                    break
                else:
                    lp()
                    print("EL RUT YA SE ENCUENTRA ASIGNADO A UN ASIENTO!")
                    mostrar_ubicaciones()

            else:
                lp()
                print("ERROR! DEBES INGRESAR UN RUT EXISTENTE!")
        except:
            lp()
            print("ERROR! DEBES INGRESAR UN NUMERO DE RUT VALIDO!")
        

def validar_asiento(cant):
    global cont_silver,cont_gold,cont_platinum
    i = 0
    while i < cant:
        print(f"\nASIGNANDO ASIENTO {i+1} DE {cant}")
        mostrar_ubicaciones()
        solicitado = int(input("\nINGRESE ASIENTO\n\t>>> "))
        if solicitado in ubicaciones:
            for x in range(10):
                for y in range(10):
                    if ubicaciones[x][y] == solicitado:
                        ubicaciones[x][y] = 0
                        i = i + 1
                        validar_rut()
                        lista_asiento.append(solicitado)
                        if x>=0 and x<=1:
                            lista_venta.append(int(120000))
                            cont_platinum=cont_platinum+1
                        elif x>=2 and x<=4:
                            lista_venta.append(int(80000))
                            cont_gold=cont_gold+1
                        else:
                            cont_silver=cont_silver+1
                            lista_venta.append(int(50000))

                        lp()
                        print("ASIENTO ASIGNADO CON EXITO AL RUT INGRESADO\n")
                    else:
                        pass
            
        else:
            lp()
            print("ERROR! EL ASIENTO ESTÁ OCUPADO! SELECCIONE OTRO ASIENTO\n")



def comprar_entradas():
    lp()
    k = validar_cant_asientos_disponibles()
    print(F"CANTIDAD DE ASIENTOS DISPONIBLES: {100-k}")
    if k<100:
        print("COMPRAR ENTRADAS\n")
        cant_entradas=validar_entradas()
        validar_asiento(cant_entradas)
        lp()
        print("ASIENTOS COMPRADOS EXITOSAMENTE\n")
    else:
        lp()
        print("LO SENTIMOS! NO QUEDAN ASIENTOS DISPONIBLES PARA VENTA")
        
def mostrar_ubicaciones_disponibles():
    lp()
    mostrar_ubicaciones()
    input("\nPRESIONE ENTER PARA VOLVER AL MENU\n")

def ver_listado_asistentes():
    lp()
    lista_rut.sort()
    print("LISTADO DE ASISTENTES:")
    for x in range(len(lista_rut)):
        print(f"\t{x+1}. {lista_rut[x]}")
    input("\nPRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL\n")

def mostrar_ganancias_totales():
    print("GANANCIAS TOTALES\n")
    print(f"""
    ENTRADA\t\t\tCANTIDAD\t\tTOTAL
    PLATINUM\t120.000\t\t{cont_platinum}\t\t\t${cont_platinum*120000}
    GOLD\t80.000\t\t{cont_gold}\t\t\t${cont_gold*80000}
    SILVER\t50.000\t\t{cont_silver}\t\t\t${cont_silver*50000}
    TOTAL\t\t\t{cont_platinum+cont_gold+cont_silver}\t\t\t${(cont_platinum*120000)+(cont_gold*80000)+(cont_silver*50000)}""")
    input("PRESIONE ENTER PARA VOVLER AL MENU PRINCIPAL\n")

def salir():
    lp()
    print("DIEGO HERRERA, 6 DE JULIO DE 2023")
    