# =====================================================
# SISTEMA: Generador Seguro de Contraseñas
# Lenguaje: Python
#
# Arquitectura:
# - Capa de datos: caracteres disponibles
# - Capa de negocios: validaciones y generación
# - Capa de presentación: interacción con usuario
# =====================================================


# Librería para generar caracteres aleatorios
import random


# ================= CAPA DE DATOS =================

# Letras disponibles
LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Números disponibles
NUMEROS = "0123456789"

# Símbolos normales
SIMBOLOS = "!@#$%&*"

# Símbolos ambiguos (pueden confundirse visualmente)
SIMBOLOS_AMBIGUOS = "{}[]()/\\'\"`~,;.<>"

# ================= CAPA DE NEGOCIOS =================


# Función que valida la configuración ingresada
def validar_configuracion(longitud, letras, numeros, simbolos, ambiguos):

    # Verifica que la longitud sea válida
    if longitud < 8:
        return False


    # Verifica que haya seleccionado al menos una opción
    if not letras and not numeros and not simbolos and not ambiguos:
        return False


    return True
