# Inicializar un diccionario para almacenar los elementos HTML
html_elements = {"h1": [], "p": [], "h3": [], "img": [], "figcaption": []}

# Inicializar una variable para almacenar la línea requerida
figcaption_line = None

# Leer el archivo y cargar los elementos HTML
with open("imagenes/titulos.txt", "r", encoding="utf-8") as titulos_file:
    current_group = None
    for linea in titulos_file:
        # Dividir la línea por el primer colon encontrado
        partes = linea.strip().split(":", 1)
        # Verificar si hay al menos dos partes después de la división
        if len(partes) >= 2:
            elemento = partes[0]
            resto = partes[1]
            # Buscar el segundo colon en el resto
            idx_segundo_colon = resto.find(":")
            if idx_segundo_colon != -1:
                identificador = resto[:idx_segundo_colon]
                contenido = resto[idx_segundo_colon + 1:].strip()
                if elemento == "img":
                    # Si es una imagen, agregarla directamente al diccionario de elementos HTML
                    html_elements[elemento].append((identificador, contenido))
                else:
                    # Si es un título, párrafo, subtítulo o figcaption, iniciar un nuevo grupo
                    current_group = elemento
                    if elemento not in html_elements:
                        html_elements[elemento] = []
                    html_elements[elemento].append((identificador, contenido))
                
                # Buscar la línea que contiene la etiqueta <figcaption>
                if elemento == "figcaption":
                    figcaption_line = contenido
            else:
                print("Error: la línea no contiene suficientes valores después del primer colon:", linea)
        else:
            print("Error: la línea no contiene suficientes valores después del primer colon:", linea)

# Generar el contenido HTML
html_content = "<!DOCTYPE html>\n<html lang='es'>\n<head>\n<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<title>Títulos</title>\n</head>\n<body>\n"

# Obtener la cantidad de imágenes
num_img = len(html_elements["img"])

# Iterar sobre cada imagen
for i in range(num_img):
    # Agregar una etiqueta de apertura para un contenedor de artículo
    html_content += "<article class='product'>\n"
    
    # Verificar si hay un título h1 disponible para esta imagen
    if i < len(html_elements['h1']):
        html_content += f"<h2>{html_elements['h1'][i][1]}</h2>\n"
    
    # Agregar la etiqueta de apertura de la figura
    html_content += "<figure>\n"
    
    # Verificar si hay una imagen disponible para este índice
    if i < len(html_elements['img']):
        html_content += f"<img src='{html_elements['img'][i][1]}' alt=''>\n"
    
    # Verificar si hay un figurecaption disponible para esta imagen
    if figcaption_line:
        html_content += f"<figcaption>{figcaption_line}</figcaption>\n"
    
    # Agregar la etiqueta de cierre de la figura
    html_content += "</figure>\n"
    
    # Verificar si hay un párrafo disponible para esta imagen
    if i < len(html_elements['p']):
        html_content += f"<p class='nombre'>{html_elements['p'][i][1]}</p>\n"
    
    # Verificar si hay un subtítulo h3 disponible para esta imagen
    if i < len(html_elements['h3']):
        html_content += f"<p class='descripcion'>{html_elements['h3'][i][1]}</p>\n"

    # Verificar si hay un subtítulo h3 disponible para esta imagen
    if i < len(html_elements['h3']):
        html_content += f"<p class='precio'>{html_elements['h3'][i][1]}</p>\n"

    # Agregar la etiqueta de apertura del formulario con el manejador de eventos onsubmit
    html_content += "<form onsubmit='event.preventDefault(); agregarAlCarrito(this)'>\n"
    
    # Agregar el botón "Agregar al Carrito"
    html_content += "<button type='submit'>Agregar al Carrito</button>\n"

    # Agregar el botón "Ver Detalles"
    html_content += "<button type='button' onclick='openModal()'>Ver Detalles</button>\n"

    # Cerrar el formulario
    html_content += "</form>\n"
    
    # Cerrar el contenedor de artículo
    html_content += "</article>\n"

# Agregar las etiquetas de cierre </body> y </html>
html_content += "</body>\n</html>"

# Escribir el contenido HTML en un archivo
with open("xindex.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Indicar que el archivo se ha creado con éxito
print("El archivo 'index.html' se ha creado correctamente.")
