# apolonio_core.py

from agente_fiscal import AgenteFiscal
from agente_facturacion import AgenteFacturacion
from agente_recordatorios import AgenteRecordatorios


class ApolonioZanjales:
    """
    Agente principal MANU AI para un autónomo electricista
    en la Comunitat Valenciana.
    """

    def __init__(self, nombre_autonomo: str, nif: str, actividad: str = "Electricista de baja tensión"):
        self.nombre_autonomo = nombre_autonomo
        self.nif = nif
        self.actividad = actividad

        # Subagentes especializados
        self.fiscal = AgenteFiscal(self)
        self.facturacion = AgenteFacturacion(self)
        self.recordatorios = AgenteRecordatorios(self)

    def resumen_perfil(self) -> str:
        return (
            f"Apolonio Zánjales – Agente IA de {self.nombre_autonomo} "
            f"({self.actividad}, NIF: {self.nif})"
        )

    def procesar_peticion(self, texto: str) -> str:
        """
        Pseudológica muy simple:
        decide a qué subagente enviar la petición según palabras clave.
        """

        texto_lower = texto.lower()

        if any(p in texto_lower for p in ["iva", "303", "130", "hacienda", "trimestre"]):
            return self.fiscal.atender_consulta(texto)

        if any(p in texto_lower for p in ["factura", "facturación", "cliente", "presupuesto"]):
            return self.facturacion.atender_consulta(texto)

        if any(p in texto_lower for p in ["recordatorio", "qué toca este trimestre", "calendario"]):
            return self.recordatorios.atender_consulta(texto)

        # Respuesta por defecto
        return (
            "No tengo claro a qué área pertenece tu consulta. "
            "¿Es sobre facturas, impuestos o recordatorios trimestrales?"
        )
