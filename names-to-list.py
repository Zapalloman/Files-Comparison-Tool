import os

def obtener_lista_archivos(ruta_carpeta):
    try:
        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(ruta_carpeta)

        # Filtrar solo los archivos (no directorios)
        archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(ruta_carpeta, archivo))]

        return archivos
    except Exception as e:
        print(f"Error al obtener la lista de archivos: {e}")
        return None

def guardar_lista_en_archivo(lista_archivos, nombre_archivo_salida):
    try:
        with open(nombre_archivo_salida, 'w') as archivo:
            for archivo_nombre in lista_archivos:
                archivo.write(archivo_nombre + '\n')
        print(f"Lista de archivos guardada en {nombre_archivo_salida}")
    except Exception as e:
        print(f"Error al guardar la lista en el archivo: {e}")

if __name__ == "__main__":
    # Ruta de la carpeta a analizar
    ruta_carpeta = '(put your path here)'

    # Obtener la lista de archivos
    lista_archivos = obtener_lista_archivos(ruta_carpeta)

    if lista_archivos:
        # Guardar la lista en un archivo de texto
        nombre_archivo_salida = 'archive_list.txt'
        guardar_lista_en_archivo(lista_archivos, nombre_archivo_salida)
    else:
        print("No se pudo obtener la lista de archivos.")

