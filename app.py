t streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
# Cada bloque entre { } es una pregunta distinta. Cada pregunta es un diccionario de 3 entradas (texto, opciones, correcta).
# Creamos la lista de preguntas: 
preguntas = [
    {
        "texto": "¿en que año españa gano el mundial?",
        "opciones": ["2000", "2010", "2026", "1990"],
        "correcta": "2010"
    },
    {
        "texto": "¿cuantos segidores tiene jabad2 en febrero 2026?",
        "opciones": ["10m", "350", "155"],
        "correcta": "155"
    },
    {
        "texto": "¿que youtuber es mejor?",
        "opciones": ["jabad2", "gk_minemo", "the greft"],
        "correcta": "gk_minemo"
    },
    {
        "texto": "¿cuantos años lleva el legi en el colegio?",
        "opciones": ["15", "30", "124"],
        "correcta": "30"
    } ,
    {
        "texto": "¿cuando nacio Carlos V?",
        "opciones": ["1000", "1500", "2000"],
        "correcta": "1500"
    } ,
    {
        "texto": "¿cuanta vida tiene una torre de clash royale?",
        "opciones": ["2059", "3668", "3052"],
        "correcta": "3052"
    } ,
    {
        "texto": "¿cual es la carta mas rapida de clash royale?",
        "opciones": ["mini pekka", "tronco", "espiritu (cualquiera)"],
        "correcta": "tronco"
    } ,
    {
        "texto": "¿en que dia cayo el miercoles de ceniza de 2026?",
        "opciones": ["26 de enero", "18 de febrero", "20 de febrero"],
        "correcta": "18 de febrero"
    } ,
    {
        "texto": "¿pizza con piña si o no?",
        "opciones": ["no", "si"],
        "correcta": "no"
    }
]

# Configuración visual de la página
st.title("preguntas random😎🎉🎶🐱‍🐉😁👍🙌🤷‍♂️🐱‍👤")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with

with st.form("quiz_form"):

    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
    
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    # Total es número de preguntas (usa el método len)
    total = len(preguntas)

    # Comparamos las respuestas del usuario con las 'correctas' del archivador
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos = aciertos + 1

    # Calculamos la nota sobre 10
    nota = round((aciertos / total) * 10,2)
    
    
    
    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if nota >= 5:
        st.success(f"¡Felicidades! Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    if nota <= 5:
        st.success(f"muy mal eres malisimo")
        st.snow() # 
    
