from PIL import Image
import os

# Directorio de entrada y salida
directorio_entrada = "imagenes/"
directorio_salida = "datos2/"

# Obtener lista de archivos en el directorio de entrada
archivos = os.listdir(directorio_entrada)

# Lista para almacenar los nombres de los archivos
nombres_archivos = []

for archivo in archivos:
    try:
        # Ruta completa del archivo de entrada
        ruta_original = os.path.join(directorio_entrada, archivo)

        # Abrir la imagen original
        imagen_original = Image.open(ruta_original)

        # Convertir la imagen a formato JPEG
        if imagen_original.mode != "RGB":
            imagen_original = imagen_original.convert("RGB")

        # Redimensionar la imagen manteniendo la relación de aspecto 1:1 y estableciendo el tamaño en 1080x1080 píxeles
        imagen_nueva = imagen_original.resize((1080, 1920))

        # Ruta para guardar la nueva imagen con el mismo nombre que la original, pero con extensión jpg
        nombre_sin_extension = os.path.splitext(archivo)[0]
        ruta_guardado = os.path.join(directorio_salida, nombre_sin_extension + ".jpg")

        # Guardar la nueva imagen con compresión para reducir el tamaño del archivo
        calidad_predeterminada = 85  # Calidad predeterminada
        imagen_nueva.save(ruta_guardado, dpi=(72, 72), quality=calidad_predeterminada)

        # Verificar el tamaño del archivo y reducir la calidad si es necesario
        while os.path.getsize(ruta_guardado) > 800 * 1024:  # 50 KB en bytes
            calidad_predeterminada -= 5
            imagen_nueva.save(ruta_guardado, dpi=(72, 72), quality=calidad_predeterminada)

        # Agregar el nombre del archivo a la lista
        nombres_archivos.append(nombre_sin_extension)

        print(f"¡Imagen '{archivo}' convertida, redimensionada y guardada con éxito en la carpeta 'datos2'!")
    except Exception as e:
        print(f"Error al procesar la imagen '{archivo}':", e)

# Guardar los nombres de los archivos en un archivo de texto
ruta_archivo_txt = os.path.join(directorio_salida, "nombres_archivos.txt")
with open(ruta_archivo_txt, "w") as archivo_txt:
    for nombre_archivo in nombres_archivos:
        archivo_txt.write(nombre_archivo + "\n")

print("¡Nombres de archivos guardados en 'nombres_archivos.txt' en la carpeta 'datos2'!")
