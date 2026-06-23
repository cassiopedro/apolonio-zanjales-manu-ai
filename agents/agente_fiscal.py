# agente_fiscal.py

class AgenteFiscal:
    """
    Subagente encargado de IVA, IRPF y modelos de Hacienda.
    """

    def __init__(self, apolonio_core):
        self.core = apolonio_core

    def atender_consulta(self, texto: str) -> str:
        texto_lower = texto.lower()

        if "303" in texto_lower or "iva" in texto_lower:
            return self.explicar_modelo_303()

        if "130" in texto_lower or "irpf" in texto_lower:
            return self.explicar_modelo_130()

        if "036" in texto_lower or "037" in texto_lower or "alta censal" in texto_lower:
            return self.explicar_modelo_036_037()

        return "Puedo ayudarte con modelo 303 (IVA), 130 (IRPF) o 036/037 (alta censal). ¿Cuál te interesa?"

    def explicar_modelo_303(self) -> str:
        return """
MODELO 303 – IVA TRIMESTRAL

- Se declara el IVA repercutido (facturas emitidas a clientes).
- Se resta el IVA soportado (gastos deducibles).
- El resultado puede ser a ingresar, compensar o devolver.
- Plazos: abril, julio, octubre y enero.
"""

    def explicar_modelo_130(self) -> str:
        return """
MODELO 130 – IRPF ESTIMACIÓN DIRECTA

- Se declara el beneficio del trimestre (ingresos - gastos).
- Se aplica un 20% de IRPF sobre ese beneficio.
- Es un pago a cuenta de la declaración de la Renta.
"""

    def explicar_modelo_036_037(self) -> str:
        return """
MODELOS 036/037 – ALTA CENSAL

- Sirven para comunicar a Hacienda que inicias actividad como autónomo.
- Se indica el epígrafe IAE correspondiente a electricista.
- Se definen tus obligaciones: IVA, IRPF, etc.
"""
