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
