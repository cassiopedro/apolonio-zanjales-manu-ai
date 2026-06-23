# agente_facturacion.py

class AgenteFacturacion:
    """
    Subagente encargado de facturas, presupuestos y hojas de servicio.
    """

    def __init__(self, apolonio_core):
        self.core = apolonio_core

    def atender_consulta(self, texto: str) -> str:
        texto_lower = texto.lower()

        if "presupuesto" in texto_lower:
            return self.generar_presupuesto_basico()

        if "factura" in texto_lower:
            return self.generar_factura_basica()

        if "hoja de servicio" in texto_lower or "reparación" in texto_lower:
            return self.generar_hoja_servicio()

        return "Puedo ayudarte con facturas, presupuestos o hojas de servicio. ¿Qué necesitas exactamente?"

    def generar_factura_basica(self) -> str:
        """
        Devuelve una factura en texto usando la plantilla de /templates.
        (Aquí solo devolvemos texto; en la práctica podrías cargar el .md)
        """
        return f"""
FACTURA – {self.core.nombre_autonomo} (NIF: {self.core.nif})

CLIENTE:
- Nombre:
- Dirección:

TRABAJO REALIZADO:
- Descripción:
- Mano de obra: __ horas × __ €/hora
- Materiales: __ €

TOTALES:
- Base imponible: __ €
- IVA (21%): __ €
- TOTAL: __ €
"""

    def generar_presupuesto_basico(self) -> str:
        return f"""
PRESUPUESTO – {self.core.nombre_autonomo} (Electricista de baja tensión)

CLIENTE:
- Nombre:
- Dirección de la obra:

DESCRIPCIÓN DEL PROYECTO:
- Instalación / reparación a realizar

DETALLE ECONÓMICO:
- Materiales estimados: __ €
- Mano de obra estimada: __ €
- Base imponible: __ €
- IVA (21%): __ €
- TOTAL PRESUPUESTO: __ €
"""

    def generar_hoja_servicio(self) -> str:
        return """
HOJA DE SERVICIO – REPARACIÓN ELÉCTRICA

CLIENTE:
- Nombre:
- Dirección:

AVERÍA REPORTADA:
- Descripción:

TRABAJO REALIZADO:
- Detalle:

TIEMPO EMPLEADO:
- Horas: __
- Precio/hora: __ €

MATERIALES:
- Lista de materiales y precios

TOTAL:
- Mano de obra: __ €
- Materiales: __ €
- IVA (21%): __ €
- TOTAL: __ €
"""
