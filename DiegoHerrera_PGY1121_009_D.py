import funciones as fn

txt = """
BIENVENIDO AL SISTEMA
DE COMPRA DE ENTRADAS
DE CREATIVOS.CL

MENU
1. COMPRAR ENTRADAS
2. MOSTRAR UBICACIONES DISPONIBLES
3. VER LISTADO DE ASISTENTES
4. MOSTRAR GANANCIAS TOTALES
5. SALIR

"""

while True:
    fn.lp()
    print(txt)
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.comprar_entradas()
    elif opcion == 2:
        fn.mostrar_ubicaciones_disponibles()
    elif opcion == 3:
        fn.ver_listado_asistentes()
    elif opcion == 4:
        fn.mostrar_ganancias_totales()
    else:
        fn.salir()
        break