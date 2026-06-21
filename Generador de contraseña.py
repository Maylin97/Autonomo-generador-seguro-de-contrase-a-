# =====================================================
# SISTEMA: Generador Seguro de Contraseñas
# Arquitectura:
# - Presentación
# - Negocios
# - Datos
# =====================================================


import random


# ================= CAPA DE DATOS =================

# Catálogo de caracteres permitidos
LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMEROS = "0123456789"
SIMBOLOS = "!@#$%&*"
# ================= CAPA DE NEGOCIOS =================

def validar_configuracion(longitud, letras, numeros, simbolos):
    """
    Verifica que la configuración cumpla las reglas
    del sistema antes de generar la contraseña.
    """

    if longitud < 8:
        return False

    if not letras and not numeros and not simbolos:
        return False

    return True
