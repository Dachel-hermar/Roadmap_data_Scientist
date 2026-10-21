import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
P1_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "02_Flujo_Efectivo"))
if P1_DIR not in sys.path:
    sys.path.append(P1_DIR)

import database_financiero

class SimuladorIRPF:
    # Atributo de CLASE: la ley fiscal es igual para todo el mundo
    tramos = [
        (12450, 0.180),
        (13362, 0.205),
        (19004, 0.227),
        (20200, 0.248),
        (35200, 0.278),
        (35425, 0.313),
        (57320, 0.359),
        (60000, 0.390),
        (300000, 0.400),
        (float('inf'), 0.450) # 'inf' representa infinito (el último tramo)
    ]

    @classmethod
    def actualizar_tramos(cls, nuevos_tramos):
        """Permite que si el gobierno cambia la ley en 2027, 
        se actualice la clase entera sin reiniciar nada."""
        cls.tramos = nuevos_tramos

    @classmethod
    def calcular_impuesto(cls, base_imponible):
        limite_anterior=0.0
        impuesto_total = 0.0
        for limite_actual, porciento in cls.tramos:
            if base_imponible > limite_actual:
                impuesto_total+=(limite_actual - limite_anterior) * porciento
                limite_anterior = limite_actual
            else:
                impuesto_total+= (base_imponible - limite_anterior)*porciento
                break
        return round(impuesto_total,2)
    
    @classmethod
    def procesar_ingresos(cls, porcentaje_retencion=0.08):
        # 1. Traer los registros desde Supabase
        registros = database_financiero.obtener_todos_los_registros("Ingresos")
        
        total_bruto = 0.0
        total_retenciones = 0.0

        # 2. Recorrer cada fila: (concepto, monto, fecha, categoria)
        for concepto, monto, fecha, categoria in registros:
            # Pregunta: ¿Es nómina? (recuerda usar .lower() para no fallar con mayúsculas/minúsculas)
            if "nomina" in concepto.lower().replace("ó", "o"):
                
            # - Si es nómina: calculas su bruto y su retención con la fórmula
                bruto_fila = monto / (1 - porcentaje_retencion)
                retencion_fila = bruto_fila - monto

                total_bruto += bruto_fila
                total_retenciones += retencion_fila

            # - Si NO es nómina: el bruto es el monto directo y la retención es 0
            else:
                total_bruto+=monto
                

        # 3. Devolvemos los dos totales redondeados a 2 decimales
        return round(total_bruto, 2), round(total_retenciones, 2)

    @classmethod
    def procesar_deducciones(cls):
        gastos = database_financiero.obtener_todos_los_registros("Gastos")
        # el colocador filter
        gastos_alquiler = list(filter(lambda g: "alquiler" in g[0].lower(), gastos))
        #la transformacion
        deducciones_alquiler = list(map(lambda g: g[1] * 0.10, gastos_alquiler))
        # El limite legal
        total_deducciones = min(sum(deducciones_alquiler), 1000.0)
        return round(total_deducciones, 2)
    
    @classmethod
    def liquidar_ejercicio(cls):
        # 1. Ingresos y Retenciones
        bruto_total, retenciones_totales = cls.procesar_ingresos()
        
        # 2. Deducciones
        deducciones = cls.procesar_deducciones()
        
        # 3. Base Liquidable Real (Bruto menos lo que Hacienda te permite restar)
        base_liquidable = max(0.0, bruto_total - deducciones)
        
        # 4. Impuesto Teórico Anual según los tramos de Madrid
        cuota_integra = cls.calcular_impuesto(base_liquidable)
        
        # 5. La Liquidación Final: ¿Debo o me devuelven?
        resultado = round(cuota_integra - retenciones_totales, 2)
        
        # 6. Tipo Efectivo Real (%)
        tipo_efectivo = round((cuota_integra / bruto_total) * 100, 2) if bruto_total > 0 else 0.0
        
        # 7. Armar el Reporte Fiscal
        veredicto = f"Toca PAGAR a Hacienda: {resultado} €" if resultado > 0 else f"Hacienda te DEVUELVE: {abs(resultado)} €"
        if resultado == 0:
            veredicto = "En tablas: Ni pagas ni te devuelven (0.0 €)"

        reporte = f"""
        ================ LIQUIDACIÓN IRPF (MADRID) ================
        Base Imponible Bruta:        {bruto_total} €
        (-) Deducciones Aplicadas:    {deducciones} €
        -----------------------------------------------------------
        Base Liquidable:             {base_liquidable} €
        Cuota Íntegra (Impuesto):    {cuota_integra} € (Tipo medio: {tipo_efectivo}%)
        (-) Retenciones Pagadas:     {retenciones_totales} €
        ===========================================================
        RESULTADO FINAL: {veredicto}
        ===========================================================
        """
        return reporte

if __name__ == "__main__":
    print(SimuladorIRPF.liquidar_ejercicio())

                

