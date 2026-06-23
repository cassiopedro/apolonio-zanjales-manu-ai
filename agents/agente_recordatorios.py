# agente_recordatorios.py

class AgenteRecordatorios:
    """
    Subagente encargado de recordatorios fiscales y checklist trimestral.
    """

    def __init__(self, apolonio_core):
        self.core = apolonio_core

    def atender_consulta(self, texto: str) -> str:
        return self.generar_recordatorio_trimestral()

    def generar_recordatorio_trimestral(self) -> str:
        return """
RECORDATORIO TRIMESTRAL

Este trimestre deberías revisar:

- Modelo 303 (IVA)
- Modelo 130 (IRPF)
- Facturas emitidas
- Gastos deducibles
- Documentación organizada por fechas

Fechas clave:
- Abril
- Julio
- Octubre
- Enero
"""
