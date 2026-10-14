from modelos_analizador import Ingresos,Gastos, Madre

while True:
    print(f'{"=="*20}CARGANDO OPCIONES{"=="*20}')
    try:
        tabla= int(input(f"¿A quien pertenece este gasto?\n 1.Ingreso\n 2. Gastos\n "))

        if tabla==1:
            tabla=Ingresos
            departamento= "Ingresos"
        elif tabla==2:
            tabla=Gastos
            departamento= "Gastos"
        else:
            print("Opción inválida. Por favor, elige '1' o '2'.")
            continue
        
        print(f"ELIGE UNA DE LAS SIGUIENTES OPCIONES\n 1. Agregar un nuevo Registro\n 3. Ver su Dashboard de Salud Financiera (Invocando a tu método final).\n  4. Resumen de gastos totales\n 5. Valor global I/G\n 6. Consulta por categoria\n 7. Consulta por concepto\n 8. Presupuesto\n 9. Salir")
        opcion= int(input(f"Ingrese la opción de registro:  "))


        if opcion==1:
            concepto=input("Agregue el concepto:  ").title()
            monto=float(input("Agregue el monto:  "))
            fecha= input("Agregue la fecha:  ")
            categoria= input("Agregue la categoria:  ")
            nuevo_ingreso=tabla(concepto,monto,fecha,categoria)
            nuevo_ingreso.guardar_sql()

        if opcion==3:
            print(Madre.salud_financiera())
            

        if opcion==4:
            resultado=Madre.resumen_gastos_totales()
            print(f"Sus gastos totales generales para es de {resultado}")
            

        if opcion==5:
            resultado=tabla.valor_global(departamento)
            print(resultado)

        if opcion==6:
            resultado=tabla.consulta_categoria(departamento)
            print(resultado)

        if opcion==7:
            nombre= input("Ingrese el nombre del concepto a buscar:  ")
            resultado=tabla.concepto(departamento, nombre)
            print(resultado)

        if opcion== 8:
            resultado= Madre.reporte_metas()
            print(resultado)

        if opcion==9:
            print("HASTA PRONTO")
            break
                  
    except Exception as e:
        print(f"Se ha detectado un error {e}, por favor compruebe, el dato introducido")
        break
