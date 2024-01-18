import os
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read().splitlines()
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return None
    except Exception as e:
    
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")
        return None

def comparar_archivos(archivo1, archivo2):
    archivos_extra_en_archivo1 = set(archivo1) - set(archivo2)
    archivos_extra_en_archivo2 = set(archivo2) - set(archivo1)

    if archivos_extra_en_archivo1:
        print("Archivos extra en el primer archivo:")
        for archivo in sorted(archivos_extra_en_archivo1):
            print(f"  - {archivo}")

    if archivos_extra_en_archivo2:
        print("Archivos extra en el segundo archivo:")
        for archivo in sorted(archivos_extra_en_archivo2):
            print(f"  - {archivo}")

    if not archivos_extra_en_archivo1 and not archivos_extra_en_archivo2:
        print("No hay archivos extra en ninguno de los dos archivos.")

if __name__ == "__main__":
    # Nombres de los archivos a comparar
    nombre_archivo1 = '(put your first list here)'
    nombre_archivo2 = '(put your second list here)'

    # Leer los contenidos de los archivos
    contenido_archivo1 = leer_archivo(nombre_archivo1)
    contenido_archivo2 = leer_archivo(nombre_archivo2)

    if contenido_archivo1 and contenido_archivo2:
        # Comparar los archivos
        comparar_archivos(contenido_archivo1, contenido_archivo2)
