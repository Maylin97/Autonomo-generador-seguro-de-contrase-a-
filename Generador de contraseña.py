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
# Función que crea el catálogo de caracteres
def crear_catalogo(letras, numeros, simbolos, ambiguos):

    caracteres = ""


    # Agrega letras si el usuario desea
    if letras:
        caracteres += LETRAS


    # Agrega números si el usuario desea
    if numeros:
        caracteres += NUMEROS


    # Agrega símbolos normales
    if simbolos:
        caracteres += SIMBOLOS


    # Agrega símbolos ambiguos
    if ambiguos:
        caracteres += SIMBOLOS_AMBIGUOS


    return caracteres



# Función encargada de generar la contraseña
def generar_contrasena(longitud, caracteres):

    contraseña = ""


    # Bucle que genera cada carácter
    for i in range(longitud):

        # Selecciona un carácter aleatorio
        contraseña += random.choice(caracteres)


    return contraseña
# ================= CAPA DE PRESENTACIÓN =================


# Función principal del programa
def iniciar_programa():


    # Permite repetir la generación
    continuar = "SI"



    # Bucle principal del sistema
    while continuar == "SI":


        print("\n===== GENERADOR SEGURO DE CONTRASEÑAS =====")



        # Solicita longitud
        longitud = 0


        # Validación usando bucle
        while longitud < 8:

            longitud = int(
                input("Ingrese longitud (mínimo 8): ")
            )


            if longitud < 8:

                print(
                    "Error: Debe ingresar mínimo 8 caracteres"
                )



        # Preguntas al usuario

        usar_letras = input(
            "¿Usar letras? SI/NO: "
        ).upper() == "SI"



        usar_numeros = input(
            "¿Usar números? SI/NO: "
        ).upper() == "SI"



        usar_simbolos = input(
            "¿Usar símbolos? SI/NO: "
        ).upper() == "SI"



        usar_ambiguos = input(
            "¿Usar símbolos ambiguos? SI/NO: "
        ).upper() == "SI"




        # Comprueba la configuración
        if validar_configuracion(
            longitud,
            usar_letras,
            usar_numeros,
            usar_simbolos,
            usar_ambiguos
        ):



            # Crea lista de caracteres
            caracteres = crear_catalogo(
                usar_letras,
                usar_numeros,
                usar_simbolos,
                usar_ambiguos
            )



            # Genera contraseña
            contraseña = generar_contrasena(
                longitud,
                caracteres
            )



            # Muestra resultado
            print("\nContraseña generada:")
            print(contraseña)




            # Opción de copiar
            copiar = input(
                "¿Desea copiar la contraseña? SI/NO: "
            ).upper()



            if copiar == "SI":

                print(
                    "Copie manualmente la contraseña mostrada."
                )



        else:

            print(
                "Configuración inválida"
            )



        # Pregunta si desea repetir
        continuar = input(
            "\n¿Desea generar otra contraseña? SI/NO: "
        ).upper()



    print(
        "\nPrograma finalizado."
    )



# Inicio del programa
iniciar_programa()
