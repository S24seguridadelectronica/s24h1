import pandas as pd
import re

# Cargar el archivo CSV
archivo_csv = "textoarticulos/texto.csv"  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(archivo_csv)

# Función para formatear una fila en el nuevo formato
def formatear_fila(fila, contador_etiquetas):
    formato = ""
    for i, valor in enumerate(fila):
        contador_etiquetas += 1
        if i == 0:
            formato += f"h1:{contador_etiquetas}:{valor}\n"
        elif i == 1:
            # Eliminar las comillas alrededor de la ruta de la imagen
            valor = valor.replace("\n", " ")
            formato += f"img:{contador_etiquetas}:\"imagenes/{valor.strip()}.jpg\"\n"  # Utilizar 'valor' directamente aquí
        elif i == 2:
            formato += f"figcaption:{contador_etiquetas}:{valor}\n"
        elif i == 3:
            # Eliminar saltos de línea dentro del valor del párrafo
            valor = re.sub(r'\n+', ' ', valor)  # Reemplazar saltos de línea por espacios
            formato += f"p:{contador_etiquetas}:{valor.strip()}\n"  # Eliminar espacios en blanco al principio y al final
        elif i == 4:
            formato += f"h3:{contador_etiquetas}:{valor}\n"
    return formato, contador_etiquetas

# Crear el nuevo formato
nuevo_formato = "este es un ejemplo:\n"
contador_etiquetas = 0
for index, fila in df.iterrows():
    formato_fila, contador_etiquetas = formatear_fila(fila, contador_etiquetas)
    nuevo_formato += formato_fila + "\n"

# Guardar el nuevo formato en un archivo de texto
with open("nuevo_formato.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write(nuevo_formato)

print("¡Proceso completado! El nuevo formato se ha guardado en 'nuevo_formato.txt'.")
