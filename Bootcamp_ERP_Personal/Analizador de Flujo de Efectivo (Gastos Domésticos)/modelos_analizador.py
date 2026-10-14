import sys
sys.path.append(r"C:\Roadmap_data_Scientist\Bootcamp_ERP_Personal")
sys.path

from models import GastoSupermercado, GastoGato 

import database_financiero

porcentaje= lambda hemorragia,ingreso_limpio: (hemorragia/ingreso_limpio)*100
balance = lambda ingreso_limpio, hemorragia : ingreso_limpio-hemorragia

# vamos a restar los gastos
class Madre:
    def __init__(self,tabla, concepto, monto, fecha, categoria):
        self.tabla=tabla
        self.nombre=concepto
        self.valor=monto
        self.fecha=fecha
        self.categoria=categoria
        database_financiero.crear_tabla_financiera(tabla)
    
    # guardar tabla
    def guardar_sql(self):
        if self.valor <=0:
            print("Error: Precio inválido")
            return
        database_financiero.insertar_valores(self.tabla,self.nombre,self.valor,self.fecha,self.categoria)
        print("Compra registrada en el disco duro")

    @staticmethod
    def valor_global(tabla):
        """
        Agrupa el valor total global de las tablas que se le pasen como argumentos
        Args:
        tabla: nombre de las tablas
        
        """
        respuesta=database_financiero.valores_totales(tabla)
        reporte=f"Valores Totales de la tabla {tabla}\n"
        monto=respuesta[0][0]
        reporte+= f"El valor Total es de: €{monto}"
        return reporte
    
    @staticmethod
    def consulta_categoria(tabla):
        resultado=database_financiero.consultar_categorias(tabla)
        reporte=f"Desglose de tu reporte por categoría\n"
        for i in resultado:
            categoria=i[0]
            monto_total=i[1]
            reporte += f"En la {categoria} el monto total es {monto_total}"
        return reporte

    @staticmethod
    def concepto(tabla, nombre_concepto):
        resultado=database_financiero.concepto_unitario(tabla, nombre_concepto)
        reporte = f"El concepto Unitario\n"
        for item in resultado:
            concepto= item[0]
            monto= item[1]
            reporte += f"Para el {concepto} el monto es {monto}"
        return reporte

    
    # Ahora vamos a calcular o a crear el metodo para ver cuanto llevo gastado frente a mis ingresos
   
    @staticmethod
    def limpiar_texto(tupla_de_textos):
        suma_total = 0.0
        
        # CAPA 1: Abrimos la caja y sacamos reporte por reporte
        for texto_sucio in tupla_de_textos:
            
            # CAPA 2: Rompemos el reporte actual en palabras
            palabras = texto_sucio.split()
            
            # CAPA 3: Revisamos palabra por palabra
            for palabra in palabras:
                candidato = ""
                
                # CAPA 4: Letra por letra (Tu algoritmo extractor)
                for caracter in palabra:
                    if caracter.isdigit() or caracter == ".":
                        candidato += caracter
                
                try:
                    if candidato != "":
                        suma_total += float(candidato) # Lo metemos al cofre
                        break # Encontró el número. Rompe la Capa 3 y pasa al siguiente reporte de la Capa 1
                except ValueError:
                    pass
                    
        return suma_total

    @staticmethod
    def resumen_gastos_totales():
        """
        Resume
        """
        rep_super = GastoSupermercado.gasto_total("productos")
        rep_gato = GastoGato.gasto_total("gastos_gato")
        rep_gastos_2 = Gastos.valor_global("Gastos")
        textos_sucios=[rep_super,rep_gato,rep_gastos_2]
        textos_limpios=Madre.limpiar_texto(textos_sucios)
        return round(textos_limpios,2)
    
    @staticmethod
    def salud_financiera():
        hemorragia= Madre.resumen_gastos_totales()
        ingresos=Madre.valor_global("Ingresos")
        ingreso_limpio=Madre.limpiar_texto([ingresos])
        balance_calculado=balance(ingreso_limpio, hemorragia)
        try:
            porcentaje_calculado=porcentaje(hemorragia,ingreso_limpio)
        except ZeroDivisionError:
            porcentaje_calculado=0
        return f"Tu balance actual es de €{balance_calculado}. Te has pulido el {porcentaje_calculado}% de tu sueldo"
    
    @staticmethod
    def presupuesto(categoria, limite):
        report= database_financiero.insertar_valores_metas_financieras(categoria, limite) 
        return report

    @staticmethod
    def reporte_metas():
        datos = database_financiero.consultar_gastos_vs_metas()
        if not datos:
            return "No hay gastos registrados que coincidan con las metas."
        
        reporte = "--- REPORTE DE METAS VS GASTOS ---\n"
        for dato in datos:
            if dato[1] > dato[2]:
                reporte += f"En {dato[0]} gastaste €{dato[1]} de tu límite de €{dato[2]} (¡TE PASASTE!)\n"
            else:
                reporte += f"En {dato[0]} gastaste €{dato[1]} de tu límite de €{dato[2]} (TODO BIEN)\n"
        return reporte







class Ingresos(Madre):
    def __init__(self, concepto, monto, fecha, categoria):
        super().__init__("Ingresos", concepto, monto, fecha, categoria)
        

        

class Gastos(Madre):
    
    def __init__(self,concepto, monto, fecha, categoria):

        super().__init__("Gastos", concepto, monto, fecha, categoria)
 
 
if __name__=="__main__":
        
    # Creamos un par de gastos reales para que el INNER JOIN tenga qué unir:
    g1 = Gastos("Cine", 45.0, "2026-10-14", "Varios")
    g1.guardar_sql()
    g2 = Gastos("Alquiler", 400.0, "2026-10-14", "Fijos")
    g2.guardar_sql()
    
    # ¡Ahora sí, el JOIN encontrará coincidencias!
    print(Madre.reporte_metas())



      

    
    
# Ahora vamos a anlizar primeramente los gastos e ingresos por separados

    